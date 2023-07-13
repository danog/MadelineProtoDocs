---
title: "Handling updates (new messages & other events)"
description: "Update handling can be done in different ways: "
nav_order: 11
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Handling updates (new messages & other events)

Update handling can be done in different ways: 

* [Async Event driven](#async-event-driven)
  * [Self-restart on webhosts](#self-restart-on-webhosts)
* [Async Event driven multi-account](#async-event-driven-multiaccount)
* [Webhook (for HTTP APIs)](#webhook)
* [getUpdates (only for Javascript APIs)](#getUpdates)
* [Noop (default)](#noop)


## Async Event driven

[Plugins &raquo; are also supported!](https://docs.madelineproto.xyz/docs/PLUGINS.html)

<!-- cut_here examples/bot.php -->

```php
<?php declare(strict_types=1);
/**
 * Example bot.
 *
 * PHP 8.1.15+ or 8.2.4+ is required.
 *
 * Copyright 2016-2020 Daniil Gentili
 * (https://daniil.it)
 * This file is part of MadelineProto.
 * MadelineProto is free software: you can redistribute it and/or modify it under the terms of the GNU Affero General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
 * MadelineProto is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
 * See the GNU Affero General Public License for more details.
 * You should have received a copy of the GNU General Public License along with MadelineProto.
 * If not, see <http://www.gnu.org/licenses/>.
 *
 * @author    Daniil Gentili <daniil@daniil.it>
 * @copyright 2016-2023 Daniil Gentili <daniil@daniil.it>
 * @license   https://opensource.org/licenses/AGPL-3.0 AGPLv3
 * @link https://docs.madelineproto.xyz MadelineProto documentation
 */

use danog\MadelineProto\API;
use danog\MadelineProto\Broadcast\Progress;
use danog\MadelineProto\Broadcast\Status;
use danog\MadelineProto\EventHandler\Attributes\Cron;
use danog\MadelineProto\EventHandler\Attributes\Handler;
use danog\MadelineProto\EventHandler\Filter\FilterCommand;
use danog\MadelineProto\EventHandler\Filter\FilterText;
use danog\MadelineProto\EventHandler\Message;
use danog\MadelineProto\EventHandler\SimpleFilter\Incoming;
use danog\MadelineProto\Logger;
use danog\MadelineProto\Settings;
use danog\MadelineProto\Settings\Database\Mysql;
use danog\MadelineProto\Settings\Database\Postgres;
use danog\MadelineProto\Settings\Database\Redis;
use danog\MadelineProto\SimpleEventHandler;

// MadelineProto is already loaded
if (class_exists(API::class)) {
    // Otherwise, if a stable version of MadelineProto was installed via composer, load composer autoloader
} elseif (file_exists('vendor/autoload.php')) {
    require_once 'vendor/autoload.php';
} else {
    // Otherwise download an !!! alpha !!! version of MadelineProto via madeline.php
    if (!file_exists('madeline.php')) {
        copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
    }
    require_once 'madeline.php';
}
/**
 * Event handler class.
 *
 * All properties returned by __sleep are automatically stored in the database.
 */
class MyEventHandler extends SimpleEventHandler
{
    /**
     * @var int|string Username or ID of bot admin
     */
    const ADMIN = "@me"; // !!! Change this to your username !!!

    private int $adminId;

    /**
     * @var array<int, bool>
     */
    private array $notifiedChats = [];

    /**
     * Returns a list of names for properties that will be automatically saved to the session database (MySQL/postgres/redis if configured, the session file otherwise).
     */
    public function __sleep(): array
    {
        return ['notifiedChats'];
    }

    /**
     * Get peer(s) where to report errors.
     *
     * @return int|string|array
     */
    public function getReportPeers()
    {
        return [self::ADMIN];
    }
    /**
     * Initialization logic.
     */
    public function onStart(): void
    {
        $this->logger("The bot was started!");
        $this->logger($this->getFullInfo('MadelineProto'));
        $this->adminId = $this->getId(self::ADMIN);

        $this->sendMessageToAdmins("The bot was started!");
    }

    /**
     * This cron function will be executed forever, every 60 seconds.
     */
    #[Cron(period: 60.0)]
    public function cron1(): void
    {
        $this->sendMessageToAdmins("The bot is online, current time ".date(DATE_RFC850)."!");
    }

    private int $lastLog = 0;
    /**
     * Handles updates to an in-progress broadcast.
     */
    public function onUpdateBroadcastProgress(Progress $progress): void
    {
        if (time() - $this->lastLog > 5 || $progress->status === Status::FINISHED) {
            $this->lastLog = time();
            $this->sendMessageToAdmins((string) $progress);
        }
    }

    /**
     * Handle incoming updates from users, chats and channels.
     *
     * 100+ other types of onUpdate... method types are available, see https://docs.madelineproto.xyz/API_docs/types/Update.html for the full list.
     * You can also use onAny to catch all update types (only for debugging)
     * A special onUpdateCustomEvent method can also be defined, to send messages to the event handler from an API instance, using the sendCustomEvent method.
     */
    #[Handler]
    public function handleMessage(Incoming&Message $message): void
    {
        // In this example code, send the "This userbot is powered by MadelineProto!" message only once per chat.
        // Ignore all further messages coming from this chat.
        if (!isset($this->notifiedChats[$message->chatId])) {
            $this->notifiedChats[$message->chatId] = true;

            $message->reply(
                message: "This userbot is powered by [MadelineProto](https://t.me/MadelineProto)!",
                parseMode: 'Markdown'
            );
        }
    }

    #[FilterCommand('restart')]
    public function restartCommand(Incoming&Message $message): void
    {
        // If the message is a /restart command from an admin, restart to reload changes to the event handler code.
        if ($message->senderId === $this->adminId) {
            // Make sure to run in a bash while loop when running via CLI to allow self-restarts.
            $this->restart();
        }
    }

    #[FilterCommand('broadcast')]
    public function broadcastCommand(Incoming&Message $message): void
    {
        // We can broadcast messages to all users.
        if ($message->senderId === $this->adminId) {
            if (!$message->replyToMsgId) {
                $message->reply("You should reply to the message you want to broadcast.");
                return;
            }
            $this->broadcastForwardMessages(
                from_peer: $message->senderId,
                message_ids: [$message->replyToMsgId],
                drop_author: true,
                pin: true,
            );
            return;
        }
    }

    #[FilterText('hi')]
    public function pingCommand(Incoming&Message $message): void
    {
        $message->reply('hello');
    }

    public static function getPluginPaths(): string|array|null
    {
        return 'plugins/';
    }
}

$settings = new Settings;
$settings->getLogger()->setLevel(Logger::LEVEL_ULTRA_VERBOSE);

// You can also use Redis, MySQL or PostgreSQL
// $settings->setDb((new Redis)->setDatabase(0)->setPassword('pony'));
// $settings->setDb((new Postgres)->setDatabase('MadelineProto')->setUsername('daniil')->setPassword('pony'));
// $settings->setDb((new Mysql)->setDatabase('MadelineProto')->setUsername('daniil')->setPassword('pony'));

// For users or bots
MyEventHandler::startAndLoop('bot.madeline', $settings);

// For bots only
// MyEventHandler::startAndLoopBot('bot.madeline', 'bot token', $settings);

```

<!-- cut_here_end examples/bot.php -->

[Plugins &raquo; are also supported!](https://docs.madelineproto.xyz/docs/PLUGINS.html)

This will create an event handler class `MyEventHandler`, create a MadelineProto session, and set the event handler class to our newly created event handler.

The **new** `startAndLoop` method automatically initializes MadelineProto, **enables async**, logs in the user/bot, initializes error reporting, catches and reports all errors surfacing from the event loop to the peers returned by the `getReportPeers` method.

All events are handled concurrently thanks to async, [here's a full explanation](ASYNC.html).  

When an [Update](https://docs.madelineproto.xyz/API_docs/types/Update.html) is received, the corresponding `onUpdateType` event handler method is called.  

To get a list of all possible update types, [click here](https://docs.madelineproto.xyz/API_docs/types/Update.html). 

A special `onUpdateCustomEvent` method can also be defined, to send messages to the event handler from an API instance, using the `sendCustomEvent` method.

If such a method does not exist, the `onAny` event handler method is called.  
If the `onAny` event handler method does not exist, the update is ignored.  

To access the `$MadelineProto` instance inside of the event handler, simply access `$this`:
```php
$this->messages->sendMessage(['peer' => '@danogentili', 'message' => 'hi']);
```

All property names returned by the `__sleep` method will be persisted in the database/session file.  

To forcefully restart and apply changes made to the event handler class, call `$this->restart();`.  

### Self-restart on webhosts

When running the event handler via web, MadelineProto will automatically enable a **magical self-restart hack** (callback ID `restarter`), to keep the bot running even on webhosts with limited execution time.  

Locking will also be handled automatically (as well as disconnection from the user that opened the page), so even if you start the script via web several times, only one instance will be running at a time (no need to do flocking manually!).  

It relies on the shutdown function, so you must not set a custom shutdown function in your code, and instead use the **MadelineProto shutdown static API**:  

```php
use danog\MadelineProto\Shutdown;

$id = Shutdown::addCallback(static function () {
    // This function will run on shutdown
});

$id = Shutdown::addCallback(static function () {
    // This function will run on shutdown
}, 'custom id');

$id = Shutdown::addCallback(static function () {
    // This function will overwrite the previously set function with custom id
}, 'custom id');

$ok = Shutdown::removeCallback($id);
```

You can of course pass non-static functions, any type of callable is accepted.  
A second optional parameter can also be accepted, containing the ID of the callable: you can use this if you want to later overwrite the callable with another callback, or remove it altogether.  

The `removeCallback` will return true if the callback exists and it was removed correctly, false otherwise (as with all new MadelineProto APIs, there are PHPDOCs for these methods so you'll see them in your IDE).


## Async event driven (multiaccount)

```php
use danog\MadelineProto\EventHandler;
use danog\MadelineProto\Tools;
use danog\MadelineProto\API;
use danog\MadelineProto\Logger;
use danog\MadelineProto\RPCErrorException;

// Normal event handler definition as above

$MadelineProtos = [];
foreach ([
    'bot.madeline' => 'Bot Login',
    'user.madeline' => 'Userbot login',
    'user2.madeline' => 'Userbot login (2)'
] as $session => $message) {
    Logger::log($message, Logger::WARNING);
    $MadelineProtos []= new API($session);
}

API::startAndLoopMulti($MadelineProtos, MyEventHandler::class);
```

This will create an event handler class `EventHandler`, create a **combined** MadelineProto session with session files `bot.madeline`, `user.madeline`, `user2.madeline`, and set the event handler class to our newly created event handler.

Usage is the same as for [the normal event handler](#async-event-driven), with the difference is that multiple accounts can receive and handle updates in parallel, each with its own event handler instance.

To dynamically start a new event handler, use `\Revolt\EventLoop::queue(MyEventHandler::startAndLoop(...), 'session.madeline', $settings))`.  

## Noop

```php
$MadelineProto = new \danog\MadelineProto\API('bot.madeline');

$MadelineProto->start();
$MadelineProto->setNoop();
```
When an [Update](https://docs.madelineproto.xyz/API_docs/types/Update.html) is received, nothing is done. This is useful if you need to populate the internal peer database with peers to avoid `This peer is not present in the internal peer database errors`, but don't need to handle updates.  
This is the default.  

## Webhook

Useful when consuming MadelineProto updates through an API, **not recommended when directly writing MadelineProto bots**.  

```php
$MadelineProto = new \danog\MadelineProto\API('bot.madeline');

$MadelineProto->setWebhook('https://example.com');
```

## getUpdates

Only useful when consuming MadelineProto updates through an API in another language (like Javascript), **absolutely not recommended when directly writing MadelineProto bots**.  

`getUpdates` will **greatly slow down your bot** if used directly inside of PHP code.  

**Only use the [event handler](#async-event-driven) when writing a MadelineProto bot**, because update handling in the **event handler** is completely parallelized and non-blocking.

```php
$MadelineProto = new \danog\MadelineProto\API('bot.madeline');

// NOT recommended when directly writing MadelineProto bots.
// ONLY use when exposing updates via an HTTP API to another language (like Javascript).

// DO NOT use this to handle updates in PHP code, it will cause crashes.

// Same parameters as for bot API getUpdates
echo json_encode($MadelineProto->getUpdates($_GET));
```

<a href="https://docs.madelineproto.xyz/#very-complex-and-complete-examples">Next section</a>