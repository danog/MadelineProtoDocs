---
title: "Handling updates (new messages & other events)"
description: "Update handling can be done in different ways: "
nav_order: 11
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Handling updates (new messages & other events)

Update handling can be done in different ways: 

* [Async Event driven](#async-event-driven)
  * [Full example](#async-event-driven)
  * [Bound methods](#bound-methods)
  * [Filters](https://docs.madelineproto.xyz/docs/FILTERS.html)
    * [Simple filters](https://docs.madelineproto.xyz/docs/FILTERS.html#simple-filters)
    * [Attribute filters](https://docs.madelineproto.xyz/docs/FILTERS.html#attribute-filters)
    * [MTProto filters](https://docs.madelineproto.xyz/docs/FILTERS.html#mtproto-filters)
  * [Plugins](https://docs.madelineproto.xyz/docs/PLUGINS.html)
  * [Cron](#cron)
  * [Persisting data and IPC](#persisting-data-and-ipc)
  * [Restarting](#restarting)
  * [Self-restart on webhosts](#self-restart-on-webhosts)
  * [Multi-account](#multiaccount)
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
use danog\MadelineProto\EventHandler\Filter\FilterRegex;
use danog\MadelineProto\EventHandler\Filter\FilterText;
use danog\MadelineProto\EventHandler\Message;
use danog\MadelineProto\EventHandler\SimpleFilter\FromAdmin;
use danog\MadelineProto\EventHandler\SimpleFilter\Incoming;
use danog\MadelineProto\Logger;
use danog\MadelineProto\ParseMode;
use danog\MadelineProto\Settings;
use danog\MadelineProto\Settings\Database\Mysql;
use danog\MadelineProto\Settings\Database\Postgres;
use danog\MadelineProto\Settings\Database\Redis;
use danog\MadelineProto\SimpleEventHandler;

use function Amp\File\read;

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

        $this->sendMessageToAdmins("The bot was started!");
        $this->sendMessage(
            peer: 'danogentili',
            message: read(__DIR__.'/../CHANGELOG.html'),
            parseMode: ParseMode::MARKDOWN
        );
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
    public function restartCommand(Incoming & Message & FromAdmin $message): void
    {
        // If the message is a /restart command from an admin, restart to reload changes to the event handler code.

        // Make sure to run in a bash while loop when running via CLI to allow self-restarts.
        $this->restart();
    }

    #[FilterCommand('broadcast')]
    public function broadcastCommand(Incoming & Message & FromAdmin $message): void
    {
        // We can broadcast messages to all users.
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
    }

    #[FilterCommand('echo')]
    public function echoCmd(Incoming & Message $message): void
    {
        // Contains the arguments of the command
        $args = $message->commandArgs;

        $message->reply($args[0] ?? '');
    }

    #[FilterRegex('/.*(mt?proto).*/i')]
    public function testRegex(Incoming & Message $message): void
    {
        $message->reply("Did you mean to write MadelineProto instead of ".$message->matches[1].'?');
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

The example code above defines an event handler class `MyEventHandler`, creates a MadelineProto session, and sets the event handler class to our newly created event handler.

The **new** `startAndLoop` method automatically initializes MadelineProto, **enables async**, logs in the user/bot, initializes error reporting, catches and reports all errors surfacing from the event loop to the peers returned by the `getReportPeers` method.

All events are handled concurrently thanks to async, [here's a full explanation](ASYNC.html).  

To access the `$MadelineProto` instance inside of the event handler, simply access `$this`:
```php
$this->messages->sendMessage(['peer' => '@danogentili', 'message' => 'hi']);
```

### Bound methods

MadelineProto offers a large number of helper bound methods and properties, depending on the filter type you specify in the typehint of `#[Handler]` methods.  

See [here &raquo;](https://docs.madelineproto.xyz/docs/FILTERS.html#simple-filters) for more info on how to use bound methods, properties and filters.  

Here's a full list of the concrete object types on which bound methods and properties are defined:

<!-- cut_here concretefilters -->

* [danog\MadelineProto\EventHandler\AbstractMessage &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/AbstractMessage.html) - Represents an incoming or outgoing message.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/AbstractMessage.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/AbstractMessage.html#method-list)
* [danog\MadelineProto\EventHandler\Message &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message.html) - Represents an incoming or outgoing message.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message.html#method-list)
* [danog\MadelineProto\EventHandler\Message\ServiceMessage &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/ServiceMessage.html) - Represents info about a service message.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/ServiceMessage.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/ServiceMessage.html#method-list)
* [danog\MadelineProto\EventHandler\Message\ChannelMessage &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/ChannelMessage.html) - Represents an incoming or outgoing channel message.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/ChannelMessage.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/ChannelMessage.html#method-list)
* [danog\MadelineProto\EventHandler\Message\GroupMessage &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/GroupMessage.html) - Represents an incoming or outgoing group message.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/GroupMessage.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/GroupMessage.html#method-list)
* [danog\MadelineProto\EventHandler\Message\PrivateMessage &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/PrivateMessage.html) - Represents an incoming or outgoing private message.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/PrivateMessage.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/PrivateMessage.html#method-list)
* [danog\MadelineProto\EventHandler\Message\ServiceMessage &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/ServiceMessage.html) - Represents info about a service message.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/ServiceMessage.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/ServiceMessage.html#method-list)
* [danog\MadelineProto\EventHandler\Message\Service\DialogCreated &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogCreated.html) - A chat or channel was created.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogCreated.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogCreated.html#method-list)
* [danog\MadelineProto\EventHandler\Message\Service\DialogMemberLeft &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogMemberLeft.html) - A member left the chat or channel.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogMemberLeft.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogMemberLeft.html#method-list)
* [danog\MadelineProto\EventHandler\Message\Service\DialogMembersJoined &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogMembersJoined.html) - Some members joined the chat or channel.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogMembersJoined.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogMembersJoined.html#method-list)
* [danog\MadelineProto\EventHandler\Message\Service\DialogPhotoChanged &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogPhotoChanged.html) - The photo of the dialog was changed or deleted.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogPhotoChanged.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogPhotoChanged.html#method-list)
* [danog\MadelineProto\EventHandler\Message\Service\DialogTitleChanged &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogTitleChanged.html) - The title of a channel or group has changed.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogTitleChanged.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogTitleChanged.html#method-list)


<!-- cut_here_end concretefilters -->


### Filters

MadelineProto offers three different filter types, used to filter updates by type or other attributes, click on the following links for more info:

* [Simple filters &raquo;](https://docs.madelineproto.xyz/docs/FILTERS.html#simple-filters)
* [Attribute filters &raquo;](https://docs.madelineproto.xyz/docs/FILTERS.html#attribute-filters)
* [MTProto filters &raquo;](https://docs.madelineproto.xyz/docs/FILTERS.html#mtproto-filters)

### Plugins

Plugins are also supported, check out the [plugin docs &raquo;](https://docs.madelineproto.xyz/docs/PLUGINS.html) for more info!

### Cron

All event handler methods marked by the `danog\MadelineProto\EventHandler\Attributes\Cron` attribute are periodically invoked by MadelineProto every `period` seconds:

```php
use danog\MadelineProto\EventHandler\Attributes\Cron;

class MyEventHandler extends SimpleEventHandler
{
    /**
     * This cron function will be executed forever, every 60 seconds.
     */
    #[Cron(period: 60.0)]
    public function cron1(): void
    {
        $this->sendMessageToAdmins("The bot is online, current time ".date(DATE_RFC850)."!");
    }
}
```

You can also specify millisecond intervals like `0.5` (500 milliseconds).  

MadelineProto's crons are based on the [danog/loop](https://daniil.it/loop) library: the associated PeriodicLoop instance that can be used to stop or restart the loop is passed as first parameter to the cron, and can also be fetched using `$this->getPeriodicLoop('methodName')`, in this case `$this->getPeriodicLoop('cron1')`.  

### Persisting data and IPC

All property names returned by the `__sleep` method will be saved in the database/session file, and then automatically loaded when the bot is restarted.  

<!-- cut_here examples/plugins/Danogentili/PingPlugin.php -->

```php
<?php declare(strict_types=1);

namespace MadelinePlugin\Danogentili;

use danog\MadelineProto\EventHandler\Attributes\Cron;
use danog\MadelineProto\EventHandler\Filter\FilterText;
use danog\MadelineProto\EventHandler\Message;
use danog\MadelineProto\EventHandler\SimpleFilter\Incoming;
use danog\MadelineProto\PluginEventHandler;

/**
 * Plugin event handler class.
 *
 * All properties returned by __sleep are automatically stored in the database.
 */
class PingPlugin extends PluginEventHandler
{
    private int $pingCount = 0;

    private string $pongText = 'pong';

    /**
     * You can set a custom pong text from the outside of the plugin:.
     *
     * ```
     * if (!file_exists('madeline.php')) {
     *     copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
     * }
     * include 'madeline.php';
     *
     * $a = new API('bot.madeline');
     * $plugin = $a->getPlugin(PingPlugin::class);
     *
     * $plugin->setPongText('UwU');
     * ```
     *
     * This will automatically connect to the running instance of the plugin and call the specified method.
     */
    public function setPongText(string $pong): void
    {
        $this->pongText = $pong;
    }

    /**
     * Returns a list of names for properties that will be automatically saved to the session database (MySQL/postgres/redis if configured, the session file otherwise).
     */
    public function __sleep(): array
    {
        return ['pingCount', 'pongText'];
    }
    /**
     * Initialization logic.
     */
    public function onStart(): void
    {
        $this->logger("The bot was started!");
        $this->logger($this->getFullInfo('MadelineProto'));

        $this->sendMessageToAdmins("The bot was started!");
    }

    /**
     * This cron function will be executed forever, every 60 seconds.
     */
    #[Cron(period: 60.0)]
    public function cron1(): void
    {
        $this->sendMessageToAdmins("The ping plugin is online, total pings so far: ".$this->pingCount);
    }

    #[FilterText('ping')]
    public function pingCommand(Incoming&Message $message): void
    {
        $message->reply($this->pongText);
        $this->pingCount++;
    }
}

```

<!-- cut_here_end examples/plugins/Danogentili/PingPlugin.php -->

You can read and write to those properties from the outside using getter and setter methods, for example:

```php
use danog\MadelineProto\API;
use MadelinePlugin\Danogentili\PingPlugin;

if (!file_exists('madeline.php')) {
     copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$a = new API('bot.madeline');

$plugin = $a->getPlugin(PingPlugin::class);

$plugin->setPongText('UwU');
```

### Restarting

To forcefully restart and apply changes made to the event handler class, call `$this->restart();`.  

When running via cli, the bot must run in the official [docker image](https://docs.madelineproto.xyz/docs/DOCKER.html) with `restart: always` or inside of a bash while true loop in order for `restart()` to work.  

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

The `removeCallback` will return true if the callback exists and it was removed correctly, false otherwise.


### Multiaccount

```php
use danog\MadelineProto\EventHandler;
use danog\MadelineProto\Tools;
use danog\MadelineProto\API;
use danog\MadelineProto\Logger;

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

To dynamically start a new event handler in the background, use `Tools::callFork(MyEventHandler::startAndLoop(...), 'session.madeline', $settings))`.  

**Warning**: this can only be done with already logged-in sessions, if your sessions aren't logged in yet use `startAndLoopMulti`.  

```php
use danog\MadelineProto\EventHandler;
use danog\MadelineProto\Tools;

// Normal event handler definition as above

foreach ([
    'bot.madeline' => 'Bot Login',
    'user.madeline' => 'Userbot login',
    'user2.madeline' => 'Userbot login (2)'
] as $session => $message) {
    Tools::callFork(MyEventHandler::startAndLoop(...), $session);
}
```

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

<a href="https://docs.madelineproto.xyz/docs/FILTERS.html">Next section</a>