---
title: "IPC server"
description: "Scripts that don't start an event handler talk to the session through an IPC server, which can also run on its own, locally or on another machine."
nav_order: 9
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# IPC server

Scripts that don't start an event handler talk to the session through an IPC server, which can also run on its own, locally or on another machine.  

A MadelineProto session can only be used by one process at a time: when a plain script (one that doesn't call `startAndLoop`) creates an `API` instance, MadelineProto automatically starts an IPC server in a background process, which loads the session, and the script sends all its method calls to it. Later scripts connect to the same IPC server, which keeps running until the session is used by an event handler.  

This is the default, and it requires no configuration, but the IPC server can also be started separately: for example in its own docker container, with the scripts that use it in other containers or on other machines.  

* [Standalone IPC server](#standalone-ipc-server)
  * [Starting the server](#starting-the-server)
  * [Logging in](#logging-in)
  * [Event handlers](#event-handlers)
* [Connecting to a standalone IPC server](#connecting-to-a-standalone-ipc-server)
  * [On the same machine](#on-the-same-machine)
  * [Remote IPC servers](#remote-ipc-servers)
  * [Behind a reverse proxy](#behind-a-reverse-proxy)
  * [Files](#files)
* [Docker](#docker)
* [Security](#security)

## Standalone IPC server

### Starting the server

Run the standalone IPC server of a session with:

```bash
# With the phar
php madeline.phar madeline-server /path/to/session.madeline

# With composer
php vendor/danog/madelineproto/src/Ipc/Runner/entry.php madeline-server /path/to/session.madeline

# In the official docker image, by default with the /data/session.madeline session
madeline-server /data/session.madeline
```

It runs in the foreground, logs to standard output, and saves the session and exits cleanly when it receives SIGTERM or SIGINT (so it can be run by docker, systemd or any other supervisor).  

It is configured with environment variables:

* `MADELINE_IPC_LISTEN`: comma-separated endpoints on which to accept [remote clients](#remote-ipc-servers), for example `tcp://0.0.0.0:6100,http://0.0.0.0:8080`. Without it, only clients on the same machine can connect, through the IPC socket in the session folder.
* `MADELINE_IPC_SECRET`: the shared secret of the remote clients, required with `MADELINE_IPC_LISTEN`, see [security](#security).
* `MADELINE_API_ID` and `MADELINE_API_HASH`: the [API ID and hash](https://docs.madelineproto.xyz/docs/LOGIN.html#getting-permission-to-use-the-telegram-api), required to create the session if it doesn't exist yet.

The environment variables replace the endpoints and the secret stored in the session every time the server starts.  

The same settings can also be set from PHP, in the `Ipc` settings of any instance of the session ([full reference &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/Settings/Ipc.html)): they're stored in the session like the other settings, so even the IPC servers that are started automatically, and event handlers, then accept remote clients.

```php
use danog\MadelineProto\Settings\Ipc;

$settings = (new Ipc)
    ->setListen(['tcp://0.0.0.0:6100'])
    ->setSecret(getenv('MADELINE_IPC_SECRET'));
```

### Logging in

The standalone IPC server doesn't log in by itself: log in once from a client (on the same machine or a remote one), as usual:

```php
$MadelineProto = new \danog\MadelineProto\API('session.madeline', $settings);
$MadelineProto->start();
```

The login prompts are shown by the client, and the session is stored by the server.  

### Event handlers

The IPC server runs in every process that uses the session, event handlers included: to run an event handler and also accept remote clients, simply start it with `startAndLoop` as usual, with the `Ipc` settings shown above, instead of running `madeline-server`.  

Clients connecting to a standalone IPC server (with autostart disabled, or with a remote endpoint) can't start event handlers, since they can't load the session: `startAndLoop` throws an exception, start the event handler on the server instead.

## Connecting to a standalone IPC server

### On the same machine

Disable autostart to only connect to the IPC server of the session folder, without ever starting it:

```php
use danog\MadelineProto\API;
use danog\MadelineProto\Settings;

$settings = new Settings;
$settings->getIpc()->setAutostart(false);

$MadelineProto = new API('/path/to/session.madeline', $settings);
```

If the IPC server isn't running yet, the client waits for it for up to 60 seconds, then throws an exception.  
Once connected, if the IPC server is restarted, the client waits for it to come back up (however long it takes), and its pending calls are sent again.

### Remote IPC servers

Set the endpoint of the IPC server (one of the endpoints it [listens on](#starting-the-server)) and its secret:

```php
use danog\MadelineProto\API;
use danog\MadelineProto\Settings;

$settings = new Settings;
$settings->getIpc()
    ->setEndpoint('tcp://madeline:6100')
    ->setSecret(getenv('MADELINE_IPC_SECRET'));

// The session is stored by the server: the name only identifies the client, no files are created locally
$MadelineProto = new API('session.madeline', $settings);

$MadelineProto->sendMessage(peer: '@danogentili', message: 'Hi from a remote IPC client!');
```

The supported endpoints are:

* `tcp://host:port`: a raw TCP connection, for servers listening on `tcp://`.
* `http://host:port/path`: an HTTP/1.1 connection, upgraded to the IPC protocol, for servers listening on `http://` (any path is accepted).
* `https://host/path`: the same, through a reverse proxy that terminates TLS, see below.

The connection is authenticated and encrypted in all cases, see [security](#security).  

Clients with the wrong secret fail immediately with an exception.

### Behind a reverse proxy

IPC servers listening on `http://` can be exposed through any reverse proxy that forwards HTTP upgrades, like it does for websockets: the upgrade token is `madelineproto-ipc`.  

For example, with nginx:

```nginx
location /madeline {
    proxy_pass http://madeline:8080;
    proxy_http_version 1.1;
    proxy_set_header Upgrade $http_upgrade;
    proxy_set_header Connection "upgrade";
    # IPC connections are long-lived
    proxy_read_timeout 1d;
    proxy_send_timeout 1d;
}
```

Clients then use `https://example.com/madeline` as endpoint.  

Caddy forwards upgrades automatically (`reverse_proxy madeline:8080`).

### Files

Remote IPC servers can't open the files of the clients: with a remote endpoint, files of the client machine (`LocalFile` objects and paths that exist on the client) are read by the client and streamed to the server, and `downloadToFile`/`downloadToDir` write to the client machine.  

Paths that don't exist on the client are still passed to the server, to upload its own files.  

URLs (`RemoteUrl`) and Telegram files are always handled by the server.

## Docker

The official docker image contains `madeline.phar` at `/usr/local/lib/madelineproto/madeline.phar`, and the `madeline-server` command: see [here &raquo;](https://docs.madelineproto.xyz/docs/DOCKER.html#standalone-ipc-server) for a complete `docker-compose.yml` example.

## Security

The IPC protocol exchanges serialized PHP objects: a client has full control over the session, and over the IPC server (and vice versa), so:

* Only expose IPC servers with a strong random secret, for example generated with `openssl rand -hex 32`: the secret must be at least 16 bytes long, but it isn't stretched, so short or guessable secrets could be guessed offline by someone recording a connection.
* Only connect clients to IPC servers you control.
* Changing the secret of a running server (by restarting `madeline-server` with a new `MADELINE_IPC_SECRET`, or with the settings) disconnects the clients authenticated with the previous secret.

Both sides prove that they know the secret (with an HMAC challenge-response on fresh random nonces), before anything is exchanged: all messages are then encrypted and authenticated with AES-256-GCM, with separate keys for each direction, and nothing is unserialized from a peer that couldn't be authenticated.  

The IPC socket in the session folder (used without remote endpoints) is only protected by the permissions of the session folder.

<a href="https://docs.madelineproto.xyz/docs/METRICS.html">Next section</a>