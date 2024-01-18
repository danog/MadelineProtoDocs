---
title: "FAQ"
description: "Here's a list of common MadelineProto questions and answers."
nav_order: 28
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# FAQ

Here's a list of common MadelineProto questions and answers.

## How does the MadelineProto session work?

MadelineProto's session folder contains a large amount of information needed for MadelineProto to work.  

This information can be stored:

* In RAM (default), saved to the session files every 30 seconds and on shutdown.  
* On MySQL/Postgres/Redis, according to the [database settings &raquo;](https://docs.madelineproto.xyz/docs/DATABASE.html).  

The default in-RAM storage is the fastest, but obviously uses much more memory than the MySQL/Postgres backends.  

The session data consists of multiple databases, used to greatly improve performance and reduce [flood waits](https://docs.madelineproto.xyz/docs/FLOOD_WAIT.html) through caching.  

Some of these databases *optionally* be disabled according to the [database settings &raquo;](https://docs.madelineproto.xyz/docs/DATABASE.html), in order to use less RAM/disk space: however, this usually leads to performance issues, increased flood waits (& bans) and disabled MadelineProto features, so please avoid tweaking the database configuration unless absolutely necessary.  

* Authorization & **session keys** to identify and communicate with Telegram's MTProto servers.  
* Peer database, containing the **access hash** (needed to interact with users and chats via MTProto) and other information (name, type & other info returned by getInfo/getFullInfo) about chats and users met during normal operation.  

  Without the **access hash** handled automatically by MadelineProto's peer database, you wouldn't be able to interact with users and chats by using their ID: for this reason, completely disabling the peer database **is not allowed**.  
  
  However, through the [database settings &raquo;](https://docs.madelineproto.xyz/docs/DATABASE.html), the peer database can be *optionally* configured to only store the **access hash+basic info**, or just the **access hash**, without all the extra information: this will break `getInfo`/`getFullInfo` and other MadelineProto features that rely on it, like the [event handler](https://docs.madelineproto.xyz/docs/UPDATES.html).  

* Username database, used by MadelineProt to map usernames to IDs for quicker `@username` lookups.  
  
  Through the [database settings &raquo;](https://docs.madelineproto.xyz/docs/DATABASE.html), the username database can be *optionally* disabled, completely disabling and breaking username resolution in all MadelineProto methods.  

* Min database, containing min peer location information.

  MadelineProto uses the min database automatically to populate the peer database when working with [min peers](https://core.telegram.org/api/min).  

  Through the [database settings &raquo;](https://docs.madelineproto.xyz/docs/DATABASE.html), the min database can be *optionally* disabled, which can lead to `PeerNotInDbException` exceptions when working with certain peers.  

* File reference database, containing location information about files

  MadelineProto uses the file database automatically to populate expired [file references](https://core.telegram.org/api/file_reference) when downloading and resending files.  

  Through the [database settings &raquo;](https://docs.madelineproto.xyz/docs/DATABASE.html), the file reference database can be *optionally* disabled, which can lead to `FILE_REFERENCE_*` errors when working with files.  

* Secret chat database, containing [secret chat](https://docs.madelineproto.xyz/docs/SECRET_CHATS.html) info&messages.  

This session structure is very similar to the structure of official graphical clients: all official clients use the same databases in order to work, and sometimes have even more databases for other purposes.  

Some third-party unofficial clients with very few abstractions, however, only store the session keys, allowing users to export the session as a "string session".  

This mode is not provided by MadelineProto for a number of reasons:

* **The most important reason**: Telegram **does not allow using the same auth keys from two clients at the same time**.  
  This is a very important detail: if Telegram's servers detect 2+ connections that use the same copied string session, the session is automatically deleted, emitting an `AUTH_KEY_DUPLICATED` error.   

* Providing just the auth keys as a string session will completely break almost all MadelineProto abstractions, caching and all the other features which make MadelineProto so fast and easy to use.  
* A string session containing even just auth keys + the peer database will be too large to store manually.


Another detail worth exploring is the concept 

## Why did I get a AUTH_KEY_DUPLICATED error?

This error happened because you copied the session folder, and started another parallel instance of MadelineProto on the new copied folder.  

To avoid it, avoid copying the session folder, and instead login again.  

The reason why the error is emitted is simple: Telegram **does not allow using the same auth keys from two clients at the same time**.  

If Telegram's servers detect 2+ connections that use the same auth key, the session is automatically deleted, emitting an `AUTH_KEY_DUPLICATED` error.   

This is usually **not a problem for MadelineProto**, because the session folder is exclusively locked, allowing only one special instance of MadelineProto to use the auth keys and handle requests from all client MadelineProto processes: this special server instance of MadelineProto is the  **MadelineProto IPC server**.  

When more than one or more **client** instances of MadelineProto are created using `new API`, they all asynchronously forward requests to the same **MadelineProto IPC server** using IPC (UNIX sockets on Linux/UNIX, TCP sockets on Windows).  

This allows MadelineProto to:

* Avoid the `AUTH_KEY_DUPLICATED` errors, by opening only one MTProto connection from a single MadelineProto IPC server instance.  
* Asynchronously handle requests from multiple parallel client processes, **without waiting** for the previous request to finish in order to handle the next one.  


#### How do I start the MadelineProto IPC server?

The MadelineProto IPC server is started automatically by client instances when running `new API` (if it is not already running).  

However, if an [event handler](https://docs.madelineproto.xyz/docs/UPDATES.html) is configured, it will automatically act as a MadelineProto IPC server, and client instances will **not** be able to start it: it must be kept running in order to handle requests from `new API` instances.


## What is the "MadelineProto worker" process, can I kill it?

No, you must never kill it.  

The MadelineProto worker process is like apache2: it keeps running in the background, waiting for incoming requests from MadelineProto.  

Don't kill it, or else MadelineProto will take 30+ seconds to start, every time you make a request.  

You don't kill your apache2/nginx webserver just because there are no incoming requests, and the same goes for the MadelineProto worker process.  

When there are no incoming requests, CPU usage is extremely low (`~0%`), and RAM usage can be reduced by using the [database](#how-do-i-use-a-database-in-madelineproto) (don't forget to use `updateSettings` to update the settings).  

## How do I solve "Fiber stack allocate failed" and "Fiber stack protect failed" errors?

The PHP engine mmap's two memory regions for each forked green thread: one for the stack, and one for the final guard page.  

This error is emitted when the maximum number of configured mmap'ed regions is reached: you must increase the vm.max_map_count kernel config to 262144 to fix.  

To fix, run the following command as root:

```bash
echo 262144 | sudo tee /proc/sys/vm/max_map_count
```

To persist the change across reboots:

```bash
echo vm.max_map_count=262144 | sudo tee /etc/sysctl.d/40-madelineproto.conf
```

On Windows and WSL, increasing the size of the pagefile might help; please switch to native Linux if the issue persists.

## How do I get the chat ID and/or sender ID of a message in the event handler?

Use this code:

```php
// Chat ID
$id = $this->getId($update);

// Sender ID, not always present
from_id = isset($update['message']['from_id'])
    ? $this->getId($update['message']['from_id'])
    : null;
```

## How do I extract the ID of a message sent using sendMessage/sendMedia/etc...?

Use this code:

```php
$id = $MadelineProto->extractMessageId(
    $MadelineProto->messages->sendMessage(peer: 'danogentili', message: 'test')
);
```

## How do I execute a function periodically (like cron)?

Use this code:

```php
use danog\MadelineProto\EventHandler;
use danog\MadelineProto\Settings;
use danog\Loop\GenericLoop;

class MyEventHandler extends EventHandler
{
    private PeriodicLoop $cron1;

    public function onStart(): void
    {
        // Execute every 1.0 seconds
        $this->cron1 = new PeriodicLoop($this->cron1(...), "Cron 1", 1.0);
        $this->cron1->start();
    }

    /**
     * Cron function 1.
     * Executed every second.
     */
    private function cron1(): bool
    {
        $this->echo("Current time: ".time().PHP_EOL);

        // The loop can be stopped from the outside by calling $this->cron1->stop();

        // You can also return true here to stop the loop from the inside.
        return false;
    }
}

$settings = new Settings;

MyEventHandler::startAndLoop('bot.madeline', $settings);
```

See the [danog/loop](https://daniil.it/loop) documentation for more info.

## Do I need cron to run MadelineProto?

Generally, you don't.  

To keep your MadelineProto bot online forever:

- If running via CLI, use [docker &raquo;](https://docs.madelineproto.xyz/docs/DOCKER.html) or a `screen while :; php bot.php;done` session.  
- If running via web: MadelineProto will self-restart automatically: however, please note that this self-restart logic may fail in case of a physical server reboot or web server/php-fpm restart, so it’s always a better idea to run via CLI, or use a cron to periodically ping the bot’s URL.

## How do I use a database in MadelineProto?

First of all, **never use PDO**.  

If you only want to reduce RAM usage of your bot, use this code:

```php
$settings = (new \danog\MadelineProto\Settings\Database\Mysql)
    ->setUri('tcp://localhost')
    ->setPassword('pass');

MyEventHandler::startAndLoop('bot.madeline', $settings);
```

You can also use Postgresql or Redis, see the [database docs for more info &raquo;](https://docs.madelineproto.xyz/docs/DATABASE.html).  

If you also want to store data of your bot in a database, use this code:

```php

use danog\MadelineProto\EventHandler;

class MyEventHandler extends EventHandler
{
    private int $messageCounter = 0;

    /** Which properties to save in the database */
    public function __sleep(): array
    {
        return ['messageCounter'];
    }

    public function onUpdateNewMessage(array $update) {
        $this->messageCounter++;
    }
}

$settings = (new \danog\MadelineProto\Settings\Database\Mysql)
    ->setUri('tcp://localhost')
    ->setPassword('pass');

MyEventHandler::startAndLoop('bot.madeline', $settings);
```

This will automatically store the `$messageCounter` property in the MySQL/postgres/redis database.  

The property can have any type (`array`, `object`, `string`, etc): there are no limits.  

If you actually want to interact with a real database using SQL queries, use the [amphp/mysql](https://github.com/amphp/mysql) library.  

## How do I use threads in MadelineProto?

You can fork a new green thread using this code:

```php
\danog\MadelineProto\Tools::callFork(function() {
    // Code to execute in forked thread
});
// Code to execute in original thread
```

Make sure to never use blocking functions in the forked thread (NO `file_get_contents`, `PDO`), only use [async amphp libraries](https://amphp.org) (i.e. [amphp/file](https://amphp.org/file), [amphp/mysql](https://amphp.org/mysql), and [so on...](https://amphp.org/installation)).  

See the [async docs &raquo;](https://docs.madelineproto.xyz/docs/ASYNC.html) for more info.  

## What is the "This peer is not present in the internal peer database" error (also known as PeerNotInDbException)?

This error indicates that a specified peer (user, chat, channel) was not found in the internal MadelineProto peer database.

This can be because the user(bot) has never seen the peer before in the dialog list or in a chat.  

This error can also be caused by an invalid ID, extracted manually from an update, instead of using the correct `$this->getID($update)` function.  

This error can also be caused by referring to a user/chat/channel by its bot API ID, *only if the (user)bot has never seen the peer before*.  
In this case, resolving a user/chat/channel `@username` with [getInfo](https://docs.madelineproto.xyz/getInfo.html) or importing an invite link with [messages.importChatInvite](https://docs.madelineproto.xyz/API_docs/methods/messages.importChatInvite.html), or (for users) enabling the [setCacheAllPeersOnStartup setting](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/Settings/Peer.html#setcacheallpeersonstartup-bool-cacheallpeersonstartup-self) will automatically cache the peer into the database, allowing you to use the bot API ID again.  

<a href="https://docs.madelineproto.xyz/docs/UPGRADING.html">Next section</a>