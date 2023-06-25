---
title: "FAQ"
description: "Here's a list of common MadelineProto questions and answers."
nav_order: 26
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# FAQ

Here's a list of common MadelineProto questions and answers.

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

No, you don't.  

To keep your MadelineProto bot online forever:

- If running via web, do nothing: MadelineProto will self-restart automatically.  
- If running via CLI, use [docker &raquo;](https://docs.madelineproto.xyz/docs/DOCKER.html).  

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

## What is the "MadelineProto worker" process, can I kill it?

No, you must never kill it.  

The MadelineProto worker process is like apache2: it keeps running in the background, waiting for incoming requests from MadelineProto.  

Don't kill it, or else MadelineProto will take 30+ seconds to start, every time you make a request.  

You don't kill your apache2/nginx webserver just because there are no incoming requests, and the same goes for the MadelineProto worker process.  

When there are no incoming requests, CPU usage is extremely low (`~0%`), and RAM usage can be reduced by using the [database](#how-do-i-use-a-database-in-madelineproto) (don't forget to use `updateSettings` to update the settings).  

## What is the "This peer is not present in the internal peer database" error (also known as PeerNotInDbException)?

This error indicates that a specified peer (user, chat, channel) was not found in the internal MadelineProto peer database.

This can be because the user(bot) has never seen the peer before in the dialog list or in a chat.  

This error can usually be fixed by enabling `setFullFetch(true)` in the [peer database settings](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/Settings/Peer.html#setfullfetch-bool-fullfetch-self).  

This error can also be caused by referring to a user/chat/channel by its bot API ID, *only if the (user)bot has never seen the peer before*.  
In this case, resolving a user/chat/channel `@username` with [getInfo](https://docs.madelineproto.xyz/getInfo.html) or importing an invite link with [messages.importChatInvite](https://docs.madelineproto.xyz/API_docs/methods/messages.importChatInvite.html) will automatically cache the peer into the database, allowing you to use the bot API ID again.  

<a href="https://docs.madelineproto.xyz/docs/USING_METHODS.html">Next section</a>