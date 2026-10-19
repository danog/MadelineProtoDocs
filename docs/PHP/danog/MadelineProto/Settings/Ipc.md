---
title: "danog\\MadelineProto\\Settings\\Ipc: IPC server settings."
description: "\nBy default, scripts that don't start an event handler automatically start an IPC server in the background\n(a worker process), and talk to it through a socket in the session folder.\n\nThe IPC server can also be started separately, locally or on another machine (for example in a docker container):\ndisable autostart to connect to the IPC server of the session folder only if it's already running, or set an\nendpoint to connect to a remote IPC server, which listens on the TCP or HTTP endpoints set with setListen.\nSee https://docs.madelineproto.xyz/docs/IPC.html for more info.\n\nRemote connections are authenticated and encrypted with a shared secret, which must be set on both sides.\n\nTo start a standalone IPC server, run `php madeline.phar madeline-server /path/to/session.madeline` (or, with\ncomposer, `vendor/bin/madeline-server /path/to/session.madeline`),\nwith the MADELINE_IPC_LISTEN (comma-separated endpoints) and MADELINE_IPC_SECRET environment variables, plus\nMADELINE_API_ID and MADELINE_API_HASH to create a new session; the docker image provides the `madeline-server`\ncommand, which serves /data/session.madeline by default.\n"
image: "https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png"
parent: "MadelineProto API"

---
# `danog\MadelineProto\Settings\Ipc`
[Back to index](../../../index.html)

> Author: Daniil Gentili <daniil@daniil.it>  
  

IPC server settings.  


By default, scripts that don't start an event handler automatically start an IPC server in the background
(a worker process), and talk to it through a socket in the session folder.

The IPC server can also be started separately, locally or on another machine (for example in a docker container):
disable autostart to connect to the IPC server of the session folder only if it's already running, or set an
endpoint to connect to a remote IPC server, which listens on the TCP or HTTP endpoints set with setListen.
See https://docs.madelineproto.xyz/docs/IPC.html for more info.

Remote connections are authenticated and encrypted with a shared secret, which must be set on both sides.

To start a standalone IPC server, run `php madeline.phar madeline-server /path/to/session.madeline` (or, with
composer, `vendor/bin/madeline-server /path/to/session.madeline`),
with the MADELINE_IPC_LISTEN (comma-separated endpoints) and MADELINE_IPC_SECRET environment variables, plus
MADELINE_API_ID and MADELINE_API_HASH to create a new session; the docker image provides the `madeline-server`
command, which serves /data/session.madeline by default.



## Constants
* `danog\MadelineProto\Settings\Ipc::MIN_SECRET_LENGTH`: Minimum length of the shared secret of remote IPC connections.


## Method list:
* [`__construct()`](#__construct)
* [`getSlow(): bool`](#getSlow)
* [`getAutostart(): bool`](#getAutostart)
* [`setAutostart(bool $autostart): \danog\MadelineProto\Settings\Ipc`](#setAutostart)
* [`getEndpoint(): ?string`](#getEndpoint)
* [`setEndpoint(?string $endpoint): \danog\MadelineProto\Settings\Ipc`](#setEndpoint)
* [`getSecret(): ?string`](#getSecret)
* [`setSecret(?string $secret): \danog\MadelineProto\Settings\Ipc`](#setSecret)
* [`getListen(): list<string>`](#getListen)
* [`setListen(list<string> $listen): \danog\MadelineProto\Settings\Ipc`](#setListen)

## Methods:
### <a name="__construct"></a> `__construct()`





### <a name="getSlow"></a> `getSlow(): bool`

Get WARNING: this will cause slow startup if enabled.



### <a name="getAutostart"></a> `getAutostart(): bool`

Get whether to automatically start the IPC server of the session if it isn't running.
  
Always false if a remote endpoint is set.  



### <a name="setAutostart"></a> `setAutostart(bool $autostart): \danog\MadelineProto\Settings\Ipc`

Set whether to automatically start the IPC server of the session if it isn't running (default: true).
  
If disabled, scripts connect to the IPC server of the session folder (or to the remote endpoint, if set)  
without ever starting it, waiting for it to come up, and fail if it doesn't.  
Disabling autostart also prevents scripts from loading the session in-process, so startAndLoop must be run  
on the server.  


Parameters:

* `$autostart`: `bool`   



### <a name="getEndpoint"></a> `getEndpoint(): ?string`

Get the remote IPC server to connect to, instead of the IPC server of the session folder.



### <a name="setEndpoint"></a> `setEndpoint(?string $endpoint): \danog\MadelineProto\Settings\Ipc`

Set the remote IPC server to connect to, instead of the IPC server of the session folder.
  
Supported endpoints are `tcp://host:port`, `http://host:port/path` and `https://host/path` (for IPC servers  
behind a reverse proxy, which must forward the `Upgrade: madelineproto-ipc` header, like for websockets).  
The server must listen on the endpoint (see setListen), and the shared secret must be set on both sides.  
  
If set, the IPC server is never started automatically, and no session files are created locally: the session  
name is only used as a local identifier of the client.  


Parameters:

* `$endpoint`: `?string`   



### <a name="getSecret"></a> `getSecret(): ?string`

Get the shared secret used to authenticate and encrypt remote IPC connections.



### <a name="setSecret"></a> `setSecret(?string $secret): \danog\MadelineProto\Settings\Ipc`

Set the shared secret used to authenticate and encrypt remote IPC connections.
  
Required to connect to a remote endpoint, and to listen on remote endpoints: anyone who knows it has full  
control over the session, so generate a long random one (for example with `openssl rand -hex 32`): it isn't  
stretched, so a short or guessable secret could be guessed offline from a recorded handshake.  
  
Client and server trust each other completely (the IPC protocol exchanges serialized PHP objects): only  
connect to servers you control.  
  
Changing the secret of a running server disconnects the clients authenticated with the previous one.  


Parameters:

* `$secret`: `?string`   



### <a name="getListen"></a> `getListen(): list<string>`

Get the endpoints on which the IPC server accepts remote connections.



### <a name="setListen"></a> `setListen(list<string> $listen): \danog\MadelineProto\Settings\Ipc`

Set the endpoints on which the IPC server accepts remote connections, in addition to the IPC socket of the
session folder.  
  
Supported endpoints are `tcp://host:port` and `http://host:port` (all paths are accepted, the secret  
authenticates clients; use a reverse proxy for TLS). Requires the shared secret.  


Parameters:

* `$listen`: `list<string>` Endpoints, for example `['tcp://0.0.0.0:6100']`  



---
Generated by [danog/phpdoc](https://phpdoc.daniil.it)
