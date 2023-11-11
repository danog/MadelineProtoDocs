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
  * [Automatic static analysis](#automatic-static-analysis)
  * [Avoiding the use of filesystem functions](#avoiding-the-use-of-filesystem-functions)
* [Webhook (for HTTP APIs)](#webhook)
* [getUpdates (only for Javascript APIs)](#getUpdates)
* [Noop (default)](#noop)


## Async Event driven

[Plugins &raquo; are also supported!](https://docs.madelineproto.xyz/docs/PLUGINS.html)

Simple example:
<!-- cut_here examples/simpleBot.php -->

```php
<?php declare(strict_types=1);

// Simple example bot.
// PHP 8.1.15+ or 8.2.4+ is required.

// Run via CLI (recommended: `screen php bot.php`) or via web.

// To reduce RAM usage, follow these instructions: https://docs.madelineproto.xyz/docs/DATABASE.html

use danog\MadelineProto\EventHandler\Attributes\Handler;
use danog\MadelineProto\EventHandler\Message;
use danog\MadelineProto\EventHandler\Plugin\RestartPlugin;
use danog\MadelineProto\EventHandler\SimpleFilter\Incoming;
use danog\MadelineProto\SimpleEventHandler;

// Load via composer (RECOMMENDED, see https://docs.madelineproto.xyz/docs/INSTALLATION.html#composer-from-scratch)
if (file_exists('vendor/autoload.php')) {
    require_once 'vendor/autoload.php';
} else {
    // Otherwise download an !!! alpha !!! version of MadelineProto via madeline.php
    if (!file_exists('madeline.php')) {
        copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
    }
    require_once 'madeline.php';
}

class MyEventHandler extends SimpleEventHandler
{
    // !!! Change this to your username !!!
    public const ADMIN = "@me";

    /**
     * Get peer(s) where to report errors.
     */
    public function getReportPeers()
    {
        return [self::ADMIN];
    }

    /**
     * Returns a set of plugins to activate.
     *
     * See here for more info on plugins: https://docs.madelineproto.xyz/docs/PLUGINS.html
     */
    public static function getPlugins(): array
    {
        return [
            // Offers a /restart command to admins that can be used to restart the bot, applying changes.
            // Make sure to run in a bash while loop when running via CLI to allow self-restarts.
            RestartPlugin::class,
        ];
    }

    /**
     * Handle incoming updates from users, chats and channels.
     */
    #[Handler]
    public function handleMessage(Incoming&Message $message): void
    {
        // Code that uses $message...
        // See the following pages for more examples and documentation:
        // - https://github.com/danog/MadelineProto/blob/v8/examples/bot.php
        // - https://docs.madelineproto.xyz/docs/UPDATES.html
        // - https://docs.madelineproto.xyz/docs/FILTERS.html
        // - https://docs.madelineproto.xyz/
    }
}

MyEventHandler::startAndLoop('bot.madeline');

```

<!-- cut_here_end examples/simpleBot.php -->

Advanced example:
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
use danog\MadelineProto\EventHandler\Filter\FilterTextCaseInsensitive;
use danog\MadelineProto\EventHandler\Message;
use danog\MadelineProto\EventHandler\Message\Service\DialogPhotoChanged;
use danog\MadelineProto\EventHandler\Plugin\RestartPlugin;
use danog\MadelineProto\EventHandler\SimpleFilter\FromAdmin;
use danog\MadelineProto\EventHandler\SimpleFilter\Incoming;
use danog\MadelineProto\EventHandler\SimpleFilter\IsReply;
use danog\MadelineProto\Logger;
use danog\MadelineProto\ParseMode;
use danog\MadelineProto\RemoteUrl;
use danog\MadelineProto\Settings;
use danog\MadelineProto\Settings\Database\Mysql;
use danog\MadelineProto\Settings\Database\Postgres;
use danog\MadelineProto\Settings\Database\Redis;
use danog\MadelineProto\SimpleEventHandler;
use danog\MadelineProto\VoIP;

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
 * NOTE: ALL of the following methods are OPTIONAL.
 * You can even provide an empty event handler if you want.
 *
 * All properties returned by __sleep are automatically stored in the database.
 */
class MyEventHandler extends SimpleEventHandler
{
    /**
     * @var int|string Username or ID of bot admin
     */
    public const ADMIN = "@me"; // !!! Change this to your username !!!

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
    }

    /**
     * Returns a set of plugins to activate.
     */
    public static function getPlugins(): array
    {
        return [
            // Offers a /restart command to admins that can be used to restart the bot, applying changes.
            // Make sure to run in a bash while loop when running via CLI to allow self-restarts.
            RestartPlugin::class,
        ];
    }

    /**
     * This cron function will be executed forever, every 60 seconds.
     */
    #[Cron(period: 60.0)]
    public function cron1(): void
    {
        $this->sendMessageToAdmins("The bot is online, current time ".date(DATE_RFC850)."!");
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
                parseMode: ParseMode::MARKDOWN
            );
        }
    }

    /**
     * Reposts a media file as a Telegram story.
     */
    #[FilterCommand('story')]
    public function storyCommand(Message & FromAdmin $message): void
    {
        if ($this->isSelfBot()) {
            $message->reply("Only users can post Telegram Stories!");
            return;
        }
        $media = $message->getReply(Message::class)?->media;
        if (!$media) {
            $message->reply("You should reply to a photo or video to repost it as a story!");
            return;
        }

        $this->stories->sendStory(
            peer: 'me',
            media: $media,
            caption: "This story was posted using [MadelineProto](https://t.me/MadelineProto)!",
            parse_mode: ParseMode::MARKDOWN,
            privacy_rules: [['_' => 'inputPrivacyValueAllowAll']]
        );
    }

    /**
     * Downloads all telegram stories of a user (including protected ones).
     *
     * The bot must be started via web for this command to work.
     *
     * You can also start it via CLI but you'll have to specify a download script URL in the settings: https://docs.madelineproto.xyz/docs/FILES.html#getting-a-download-link-cli-bots.
     */
    #[FilterCommand('dlStories')]
    public function dlStoriesCommand(Message $message): void
    {
        if (!$message->commandArgs) {
            $message->reply("You must specify the @username or the Telegram ID of a user to download their stories!");
            return;
        }

        $stories = $this->stories->getUserStories(user_id: $message->commandArgs[0])['stories']['stories'];
        // Skip deleted stories
        $stories = array_filter($stories, static fn (array $s): bool => $s['_'] === 'storyItem');
        // Sort by date
        usort($stories, static fn ($a, $b) => $a['date'] <=> $b['date']);

        $result = "Total stories: ".count($stories)."\n\n";
        foreach ($stories as $story) {
            $cur = "- ID {$story['id']}, posted ".date(DATE_RFC850, $story['date']);
            if (isset($story['caption'])) {
                $cur .= ', "'.self::markdownEscape($story['caption']).'"';
            }
            $result .= "$cur; [click here to download »]({$this->getDownloadLink($story)})\n";
        }

        $message->reply($result, parseMode: ParseMode::MARKDOWN);
    }

    #[FilterCommand('broadcast')]
    public function broadcastCommand(Message & FromAdmin $message): void
    {
        // We can broadcast messages to all users with /broadcast
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

    private int $lastLog = 0;
    /**
     * Handles updates to an in-progress broadcast.
     */
    #[Handler]
    public function handleBroadcastProgress(Progress $progress): void
    {
        if (time() - $this->lastLog > 5 || $progress->status === Status::FINISHED) {
            $this->lastLog = time();
            $this->sendMessageToAdmins((string) $progress);
        }
    }

    #[FilterCommand('echo')]
    public function echoCmd(Message $message): void
    {
        // Contains the arguments of the command
        $args = $message->commandArgs;

        $message->reply($args[0] ?? '');
    }

    #[FilterRegex('/.*(mt?proto)[^.]?.*/i')]
    public function testRegex(Incoming & Message $message): void
    {
        $message->reply("Did you mean to write MadelineProto instead of ".$message->matches[1].'?');
    }

    #[FilterText('test')]
    public function pingCommand(Message $message): void
    {
        $message->reply('test reply');
    }

    #[FilterCommand('react')]
    public function reactCommand(Message&IsReply $message): void
    {
        $message->getReply(Message::class)->addReaction('👌');
    }

    #[FilterCommand('unreact')]
    public function unreactCommand(Message&IsReply $message): void
    {
        $message->getReply(Message::class)->delReaction('👌');
    }

    #[FilterTextCaseInsensitive('hi')]
    public function pingCommandCaseInsensitive(Message $message): void
    {
        $message->reply('hello');
    }

    /**
     * Called when the dialog photo of a chat or channel changes.
     */
    #[Handler]
    public function logPhotoChanged(Incoming&DialogPhotoChanged $message): void
    {
        if ($message->photo) {
            $message->reply("Nice! Here's a download link for the photo: ".$message->photo->getDownloadLink());
        }
        // The group photo was deleted
    }

    /**
     * Gets a download link for any file up to 4GB!
     *
     * The bot must be started via web for this command to work.
     *
     * You can also start it via CLI but you'll have to specify a download script URL in the settings: https://docs.madelineproto.xyz/docs/FILES.html#getting-a-download-link-cli-bots.
     */
    #[FilterCommand('dl')]
    public function downloadLink(Incoming&Message $message): void
    {
        $reply = $message->getReply(Message::class);
        if (!$reply?->media) {
            $message->reply("This command must reply to a media message!");
            return;
        }
        $reply->reply("Download link: ".$reply->media->getDownloadLink());
    }

    #[FilterCommand('call')]
    public function callVoip(Incoming&Message $message): void
    {
        $this->requestCall($message->senderId)->play(new RemoteUrl('http://icestreaming.rai.it/1.mp3'));
    }

    #[Handler]
    public function handleIncomingCall(VoIP&Incoming $call): void
    {
        $call->accept()->play(new RemoteUrl('http://icestreaming.rai.it/1.mp3'));
    }

    public static function getPluginPaths(): string|array|null
    {
        return 'plugins/';
    }
}

$settings = new Settings;
$settings->getLogger()->setLevel(Logger::LEVEL_ULTRA_VERBOSE);

// You can also use Redis, MySQL or PostgreSQL.
// Data is migrated automatically.
//
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

All incoming events are **always handled**, **including old events that occurred while the script was turned off**.  

To access the `$MadelineProto` instance inside of the event handler, simply access `$this`:
```php
$this->messages->sendMessage(['peer' => '@danogentili', 'message' => 'hi']);
```

### Bound methods

MadelineProto offers a large number of helper bound methods and properties, depending on the filter type you specify in the typehint of `#[Handler]` methods.  

See [here &raquo;](https://docs.madelineproto.xyz/docs/FILTERS.html#simple-filters) for more info on how to use bound methods, properties and filters.  

Here's a full list of the concrete object types on which bound methods and properties are defined:

<!-- cut_here concretefilters -->

* [danog\MadelineProto\Broadcast\Progress &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/Broadcast/Progress.html) - Broadcast progress.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/Broadcast/Progress.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/Broadcast/Progress.html#method-list)
* [danog\MadelineProto\EventHandler\AbstractMessage &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/AbstractMessage.html) - Represents an incoming or outgoing message.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/AbstractMessage.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/AbstractMessage.html#method-list)
* [danog\MadelineProto\EventHandler\AbstractPrivateMessage &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/AbstractPrivateMessage.html) - Represents a private or secret chat message.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/AbstractPrivateMessage.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/AbstractPrivateMessage.html#method-list)
* [danog\MadelineProto\EventHandler\AbstractStory &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/AbstractStory.html) - Represents a Telegram Story.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/AbstractStory.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/AbstractStory.html#method-list)
* [danog\MadelineProto\EventHandler\BotCommands &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/BotCommands.html) - The [command set](https://core.telegram.org/api/bots/commands) of a certain bot in a certain chat has changed.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/BotCommands.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/BotCommands.html#method-list)
* [danog\MadelineProto\EventHandler\CallbackQuery &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/CallbackQuery.html) - Represents a query sent by the user by clicking on a button.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/CallbackQuery.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/CallbackQuery.html#method-list)
* [danog\MadelineProto\EventHandler\Channel\MessageForwards &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Channel/MessageForwards.html) - Indicates that the forward counter of a message in a channel has changed.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Channel/MessageForwards.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Channel/MessageForwards.html#method-list)
* [danog\MadelineProto\EventHandler\Channel\MessageViewsChanged &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Channel/MessageViewsChanged.html) - Indicates that the view counter of a message in a channel has changed.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Channel/MessageViewsChanged.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Channel/MessageViewsChanged.html#method-list)
* [danog\MadelineProto\EventHandler\Channel\UpdateChannel &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Channel/UpdateChannel.html) - A new channel is available, or info about an existing channel was changed.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Channel/UpdateChannel.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Channel/UpdateChannel.html#method-list)
* [danog\MadelineProto\EventHandler\ChatInviteRequester &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/ChatInviteRequester.html) - Indicates someone has requested to join a chat or channel.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/ChatInviteRequester.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/ChatInviteRequester.html#method-list)
* [danog\MadelineProto\EventHandler\ChatInviteRequester\BotChatInviteRequest &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/ChatInviteRequester/BotChatInviteRequest.html) - Indicates someone has requested to join a chat or channel (bots only).
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/ChatInviteRequester/BotChatInviteRequest.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/ChatInviteRequester/BotChatInviteRequest.html#method-list)
* [danog\MadelineProto\EventHandler\ChatInviteRequester\PendingJoinRequests &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/ChatInviteRequester/PendingJoinRequests.html) - Someone has requested to join a chat or channel.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/ChatInviteRequester/PendingJoinRequests.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/ChatInviteRequester/PendingJoinRequests.html#method-list)
* [danog\MadelineProto\EventHandler\Delete &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Delete.html) - Indicates that some messages were deleted.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Delete.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Delete.html#method-list)
* [danog\MadelineProto\EventHandler\Delete\DeleteChannelMessages &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Delete/DeleteChannelMessages.html) - Some messages in a [supergroup/channel](https://core.telegram.org/api/channel) were deleted.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Delete/DeleteChannelMessages.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Delete/DeleteChannelMessages.html#method-list)
* [danog\MadelineProto\EventHandler\Delete\DeleteMessages &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Delete/DeleteMessages.html) - Some messages were deleted in a private chat or simple group.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Delete/DeleteMessages.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Delete/DeleteMessages.html#method-list)
* [danog\MadelineProto\EventHandler\Delete\DeleteScheduledMessages &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Delete/DeleteScheduledMessages.html) - Some [scheduled messages](https://core.telegram.org/api/scheduled-messages) were deleted from the schedule queue of a chat.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Delete/DeleteScheduledMessages.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Delete/DeleteScheduledMessages.html#method-list)
* [danog\MadelineProto\EventHandler\InlineQuery &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/InlineQuery.html) - An incoming inline query.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/InlineQuery.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/InlineQuery.html#method-list)
* [danog\MadelineProto\EventHandler\Message &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message.html) - Represents an incoming or outgoing message.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message.html#method-list)
* [danog\MadelineProto\EventHandler\Message\ChannelMessage &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/ChannelMessage.html) - Represents an incoming or outgoing channel message.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/ChannelMessage.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/ChannelMessage.html#method-list)
* [danog\MadelineProto\EventHandler\Message\GroupMessage &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/GroupMessage.html) - Represents an incoming or outgoing group message.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/GroupMessage.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/GroupMessage.html#method-list)
* [danog\MadelineProto\EventHandler\Message\PrivateMessage &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/PrivateMessage.html) - Represents an incoming or outgoing private message.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/PrivateMessage.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/PrivateMessage.html#method-list)
* [danog\MadelineProto\EventHandler\Message\SecretMessage &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/SecretMessage.html) - Represents New encrypted message.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/SecretMessage.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/SecretMessage.html#method-list)
* [danog\MadelineProto\EventHandler\Message\ServiceMessage &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/ServiceMessage.html) - Represents info about a service message.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/ServiceMessage.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/ServiceMessage.html#method-list)
* [danog\MadelineProto\EventHandler\Message\ServiceMessage &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/ServiceMessage.html) - Represents info about a service message.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/ServiceMessage.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/ServiceMessage.html#method-list)
* [danog\MadelineProto\EventHandler\Message\Service\DialogBotAllowed &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogBotAllowed.html) - We have given the bot permission to send us direct messages.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogBotAllowed.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogBotAllowed.html#method-list)
* [danog\MadelineProto\EventHandler\Message\Service\DialogChannelCreated &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogChannelCreated.html) - The channel was created.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogChannelCreated.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogChannelCreated.html#method-list)
* [danog\MadelineProto\EventHandler\Message\Service\DialogChannelMigrateFrom &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogChannelMigrateFrom.html) - Indicates the channel was [migrated](https://core.telegram.org/api/channel) from the specified chat.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogChannelMigrateFrom.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogChannelMigrateFrom.html#method-list)
* [danog\MadelineProto\EventHandler\Message\Service\DialogChatJoinedByLink &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogChatJoinedByLink.html) - A user joined the chat via an invite link.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogChatJoinedByLink.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogChatJoinedByLink.html#method-list)
* [danog\MadelineProto\EventHandler\Message\Service\DialogChatMigrateTo &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogChatMigrateTo.html) - Indicates the chat was [migrated](https://core.telegram.org/api/channel) to the specified supergroup.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogChatMigrateTo.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogChatMigrateTo.html#method-list)
* [danog\MadelineProto\EventHandler\Message\Service\DialogContactSignUp &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogContactSignUp.html) - A contact just signed up to telegram.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogContactSignUp.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogContactSignUp.html#method-list)
* [danog\MadelineProto\EventHandler\Message\Service\DialogCreated &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogCreated.html) - A chat or channel was created.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogCreated.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogCreated.html#method-list)
* [danog\MadelineProto\EventHandler\Message\Service\DialogDeleteMessages &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogDeleteMessages.html) - Deleted messages.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogDeleteMessages.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogDeleteMessages.html#method-list)
* [danog\MadelineProto\EventHandler\Message\Service\DialogGameScore &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogGameScore.html) - Someone scored in a game.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogGameScore.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogGameScore.html#method-list)
* [danog\MadelineProto\EventHandler\Message\Service\DialogGeoProximityReached &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogGeoProximityReached.html) - A user of the chat is now in proximity of another user.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogGeoProximityReached.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogGeoProximityReached.html#method-list)
* [danog\MadelineProto\EventHandler\Message\Service\DialogGiftPremium &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogGiftPremium.html) - Info about a gifted Telegram Premium subscription.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogGiftPremium.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogGiftPremium.html#method-list)
* [danog\MadelineProto\EventHandler\Message\Service\DialogGroupCall &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogGroupCall.html) - Represents a service message about a group call.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogGroupCall.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogGroupCall.html#method-list)
* [danog\MadelineProto\EventHandler\Message\Service\DialogGroupCall\GroupCall &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogGroupCall/GroupCall.html) - The group call has started or ended.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogGroupCall/GroupCall.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogGroupCall/GroupCall.html#method-list)
* [danog\MadelineProto\EventHandler\Message\Service\DialogGroupCall\GroupCallInvited &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogGroupCall/GroupCallInvited.html) - A set of users was invited to the group call.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogGroupCall/GroupCallInvited.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogGroupCall/GroupCallInvited.html#method-list)
* [danog\MadelineProto\EventHandler\Message\Service\DialogGroupCall\GroupCallScheduled &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogGroupCall/GroupCallScheduled.html) - A group call was scheduled.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogGroupCall/GroupCallScheduled.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogGroupCall/GroupCallScheduled.html#method-list)
* [danog\MadelineProto\EventHandler\Message\Service\DialogHistoryCleared &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogHistoryCleared.html) - Chat history was cleared.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogHistoryCleared.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogHistoryCleared.html#method-list)
* [danog\MadelineProto\EventHandler\Message\Service\DialogMemberJoinedByRequest &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogMemberJoinedByRequest.html) - A user was accepted into the group by an admin.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogMemberJoinedByRequest.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogMemberJoinedByRequest.html#method-list)
* [danog\MadelineProto\EventHandler\Message\Service\DialogMemberLeft &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogMemberLeft.html) - A member left the chat or channel.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogMemberLeft.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogMemberLeft.html#method-list)
* [danog\MadelineProto\EventHandler\Message\Service\DialogMembersJoined &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogMembersJoined.html) - Some members joined the chat or channel.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogMembersJoined.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogMembersJoined.html#method-list)
* [danog\MadelineProto\EventHandler\Message\Service\DialogMessagePinned &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogMessagePinned.html) - A message was pinned in a chat.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogMessagePinned.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogMessagePinned.html#method-list)
* [danog\MadelineProto\EventHandler\Message\Service\DialogPeerRequested &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogPeerRequested.html) - Contains info about a peer that the user shared with the bot after clicking on a [keyboardButtonRequestPeer](https://docs.madelineproto.xyz/API_docs/constructors/keyboardButtonRequestPeer.html) button.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogPeerRequested.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogPeerRequested.html#method-list)
* [danog\MadelineProto\EventHandler\Message\Service\DialogPhoneCall &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogPhoneCall.html) - A phone call.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogPhoneCall.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogPhoneCall.html#method-list)
* [danog\MadelineProto\EventHandler\Message\Service\DialogPhotoChanged &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogPhotoChanged.html) - The photo of the dialog was changed or deleted.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogPhotoChanged.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogPhotoChanged.html#method-list)
* [danog\MadelineProto\EventHandler\Message\Service\DialogReadMessages &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogReadMessages.html) - Messages marked as read.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogReadMessages.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogReadMessages.html#method-list)
* [danog\MadelineProto\EventHandler\Message\Service\DialogScreenshotTaken &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogScreenshotTaken.html) - A screenshot of the chat was taken.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogScreenshotTaken.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogScreenshotTaken.html#method-list)
* [danog\MadelineProto\EventHandler\Message\Service\DialogSetChatTheme &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogSetChatTheme.html) - The chat theme was changed.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogSetChatTheme.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogSetChatTheme.html#method-list)
* [danog\MadelineProto\EventHandler\Message\Service\DialogSetChatWallPaper &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogSetChatWallPaper.html) - The [wallpaper](https://core.telegram.org/api/wallpapers) of the current chat was changed.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogSetChatWallPaper.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogSetChatWallPaper.html#method-list)
* [danog\MadelineProto\EventHandler\Message\Service\DialogSetTTL &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogSetTTL.html) - The Time-To-Live of messages in this chat was changed.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogSetTTL.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogSetTTL.html#method-list)
* [danog\MadelineProto\EventHandler\Message\Service\DialogSuggestProfilePhoto &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogSuggestProfilePhoto.html) - A new profile picture was suggested using [photos.uploadContactProfilePhoto](https://docs.madelineproto.xyz/API_docs/methods/photos.uploadContactProfilePhoto.html).
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogSuggestProfilePhoto.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogSuggestProfilePhoto.html#method-list)
* [danog\MadelineProto\EventHandler\Message\Service\DialogTitleChanged &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogTitleChanged.html) - The title of a channel or group has changed.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogTitleChanged.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogTitleChanged.html#method-list)
* [danog\MadelineProto\EventHandler\Message\Service\DialogTopicCreated &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogTopicCreated.html) - A [forum topic](https://core.telegram.org/api/forum#forum-topics) was created.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogTopicCreated.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogTopicCreated.html#method-list)
* [danog\MadelineProto\EventHandler\Message\Service\DialogTopicEdited &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogTopicEdited.html) - [Forum topic](https://core.telegram.org/api/forum#forum-topics) information was edited.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogTopicEdited.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogTopicEdited.html#method-list)
* [danog\MadelineProto\EventHandler\Message\Service\DialogWebView &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogWebView.html) - Data from an opened [reply keyboard bot web app](https://core.telegram.org/api/bots/webapps) was relayed to the bot that owns it (user & bot side service message).
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogWebView.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Message/Service/DialogWebView.html#method-list)
* [danog\MadelineProto\EventHandler\Pinned &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Pinned.html) - Indicates that some messages were pinned/unpinned.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Pinned.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Pinned.html#method-list)
* [danog\MadelineProto\EventHandler\Pinned\PinnedChannelMessages &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Pinned/PinnedChannelMessages.html) - Represents messages that were pinned/unpinned in a [channel](https://core.telegram.org/api/channel).
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Pinned/PinnedChannelMessages.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Pinned/PinnedChannelMessages.html#method-list)
* [danog\MadelineProto\EventHandler\Pinned\PinnedGroupMessages &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Pinned/PinnedGroupMessages.html) - Represents messages that were pinned/unpinned in a [chat/supergroup](https://core.telegram.org/api/channel).
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Pinned/PinnedGroupMessages.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Pinned/PinnedGroupMessages.html#method-list)
* [danog\MadelineProto\EventHandler\Pinned\PinnedPrivateMessages &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Pinned/PinnedPrivateMessages.html) - Some messages were pinned in a private chat.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Pinned/PinnedPrivateMessages.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Pinned/PinnedPrivateMessages.html#method-list)
* [danog\MadelineProto\EventHandler\Privacy &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Privacy.html) - Indicates some privacy rules for a user or set of users.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Privacy.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Privacy.html#method-list)
* [danog\MadelineProto\EventHandler\Query\ButtonQuery &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Query/ButtonQuery.html) - Represents a query sent by the user by clicking on a button.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Query/ButtonQuery.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Query/ButtonQuery.html#method-list)
* [danog\MadelineProto\EventHandler\Query\ChatButtonQuery &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Query/ChatButtonQuery.html) - Represents a query sent by the user by clicking on a button in a chat.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Query/ChatButtonQuery.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Query/ChatButtonQuery.html#method-list)
* [danog\MadelineProto\EventHandler\Query\ChatGameQuery &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Query/ChatGameQuery.html) - Represents a query sent by the user by clicking on a "Play game" button in a chat.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Query/ChatGameQuery.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Query/ChatGameQuery.html#method-list)
* [danog\MadelineProto\EventHandler\Query\GameQuery &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Query/GameQuery.html) - Represents a query sent by the user by clicking on a "Play game" button.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Query/GameQuery.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Query/GameQuery.html#method-list)
* [danog\MadelineProto\EventHandler\Query\InlineButtonQuery &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Query/InlineButtonQuery.html) - Represents a query sent by the user by clicking on a button in an inline message.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Query/InlineButtonQuery.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Query/InlineButtonQuery.html#method-list)
* [danog\MadelineProto\EventHandler\Query\InlineGameQuery &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Query/InlineGameQuery.html) - Represents a query sent by the user by clicking on a "Play game" button in an inline message.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Query/InlineGameQuery.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Query/InlineGameQuery.html#method-list)
* [danog\MadelineProto\EventHandler\Story\Story &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Story/Story.html) - Represents a Telegram story.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Story/Story.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Story/Story.html#method-list)
* [danog\MadelineProto\EventHandler\Story\StoryDeleted &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Story/StoryDeleted.html) - Represents a deleted story.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Story/StoryDeleted.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Story/StoryDeleted.html#method-list)
* [danog\MadelineProto\EventHandler\Story\StoryReaction &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Story/StoryReaction.html) - Represents a reaction to a story.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Story/StoryReaction.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Story/StoryReaction.html#method-list)
* [danog\MadelineProto\EventHandler\Typing &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Typing.html) - A user is typing.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Typing.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Typing.html#method-list)
* [danog\MadelineProto\EventHandler\Typing\ChatUserTyping &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Typing/ChatUserTyping.html) - The user is preparing a message in a group; typing, recording, uploading, etc. This update is valid for 6 seconds. If no further updates of this kind are received after 6 seconds, it should be considered that the user stopped doing whatever they were doing.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Typing/ChatUserTyping.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Typing/ChatUserTyping.html#method-list)
* [danog\MadelineProto\EventHandler\Typing\SecretUserTyping &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Typing/SecretUserTyping.html) - The user is preparing a message in a secret chat; typing, recording, uploading, etc. This update is valid for 6 seconds. If no further updates of this kind are received after 6 seconds, it should be considered that the user stopped doing whatever they were doing.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Typing/SecretUserTyping.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Typing/SecretUserTyping.html#method-list)
* [danog\MadelineProto\EventHandler\Typing\SupergroupUserTyping &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Typing/SupergroupUserTyping.html) - A user is typing in a [supergroup](https://core.telegram.org/api/channel).
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Typing/SupergroupUserTyping.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Typing/SupergroupUserTyping.html#method-list)
* [danog\MadelineProto\EventHandler\Typing\UserTyping &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Typing/UserTyping.html) - The user is preparing a message; typing, recording, uploading, etc. This update is valid for 6 seconds. If no further updates of this kind are received after 6 seconds, it should be considered that the user stopped doing whatever they were doing.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Typing/UserTyping.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/Typing/UserTyping.html#method-list)
* [danog\MadelineProto\EventHandler\User\Blocked &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/User/Blocked.html) - A peer was blocked.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/User/Blocked.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/User/Blocked.html#method-list)
* [danog\MadelineProto\EventHandler\User\BotStopped &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/User/BotStopped.html) - A bot was stopped or re-started.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/User/BotStopped.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/User/BotStopped.html#method-list)
* [danog\MadelineProto\EventHandler\User\Phone &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/User/Phone.html) - A user’s phone number was changed.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/User/Phone.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/User/Phone.html#method-list)
* [danog\MadelineProto\EventHandler\User\Status &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/User/Status.html) - Contains a status update.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/User/Status.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/User/Status.html#method-list)
* [danog\MadelineProto\EventHandler\User\Status\Emoji &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/User/Status/Emoji.html) - The [emoji status](https://core.telegram.org/api/emoji-status) of a certain user has changed or was removed.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/User/Status/Emoji.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/User/Status/Emoji.html#method-list)
* [danog\MadelineProto\EventHandler\User\Status\EmptyStatus &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/User/Status/EmptyStatus.html) - User status has not been set yet.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/User/Status/EmptyStatus.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/User/Status/EmptyStatus.html#method-list)
* [danog\MadelineProto\EventHandler\User\Status\LastMonth &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/User/Status/LastMonth.html) - Online status: last seen last month.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/User/Status/LastMonth.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/User/Status/LastMonth.html#method-list)
* [danog\MadelineProto\EventHandler\User\Status\LastWeek &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/User/Status/LastWeek.html) - Online status: last seen last week.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/User/Status/LastWeek.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/User/Status/LastWeek.html#method-list)
* [danog\MadelineProto\EventHandler\User\Status\Offline &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/User/Status/Offline.html) - The user’s offline status.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/User/Status/Offline.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/User/Status/Offline.html#method-list)
* [danog\MadelineProto\EventHandler\User\Status\Online &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/User/Status/Online.html) - Online status of the user.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/User/Status/Online.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/User/Status/Online.html#method-list)
* [danog\MadelineProto\EventHandler\User\Status\Recently &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/User/Status/Recently.html) - Online status: last seen recently.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/User/Status/Recently.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/User/Status/Recently.html#method-list)
* [danog\MadelineProto\EventHandler\User\Username &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/User/Username.html) - Changes were made to the user’s first name, last name or username.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/User/Username.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/EventHandler/User/Username.html#method-list)
* [danog\MadelineProto\VoIP &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/VoIP.html) - This update represents a VoIP Telegram call.
  * [Full property list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/VoIP.html#properties)
  * [Full bound method list &raquo;](https://docs.madelineproto.xyz/PHP/danog/MadelineProto/VoIP.html#method-list)


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
     * Plugins may be enabled or disabled at startup by returning true or false from this function.
     */
    public function isPluginEnabled(): bool
    {
        return true;
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

>Please note that this self-restart logic may fail in case of a physical server reboot or web server/php-fpm restart, so it's always a better idea to run via CLI, or use a cron to periodically ping the bot's URL.

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

### Automatic static analysis

MadelineProto will automatically analyze the event handler code, blocking execution if performance or security issues are detected!

For example, the following functions and classes are **banned**, and the specified async counterparts must be used, instead:

* `file_get_contents`, `file_put_contents`, `fopen` - Please use https://github.com/amphp/file or https://github.com/amphp/http-client, instead
* `curl_exec` - Please use https://github.com/amphp/http-client, instead
* `mysqli_query`, `mysqli_connect`, `mysql_connect`, `PDO`, `mysqli` - Please use https://github.com/amphp/mysql or https://github.com/amphp/postgres, instead
* `fsockopen` - Please use https://github.com/amphp/socket, instead


### Avoiding the use of filesystem functions

For performance reasons, it is heavily *recommended* you **do not** read files from the filesystem at all, even using async functions.  

MadelineProto does not block the usage of async file functions, but 99% of the time they can be replaced with a much faster alternative.

Here's a list of common uses for files, and what they can be replaced with:

* [Configuration](#configuration)
* [Creating and uploading text files](#creating-and-uploading-text-files)
* [Logging](#logging)

#### Configuration

Configuration can be done entirely using persistent properties, for example:

```php
<?php

use Amp\File\read;
use Amp\File\write;

// WRONG!
if (!read('online.txt')) {
    write('online.txt', 'on');
}

class OnlinePlugin extends PluginEventHandler
{
    #[Cron(period: 60.0)]
    public function cron(): void
    {
        // WRONG!
        if (read('online.txt') === 'on') {
            $this->account->updateStatus(offline: false);
        } else {
            $this->account->updateStatus(offline: true);
        }
    }
}
```

Do this, instead:

<!-- cut_here examples/plugins/Danogentili/OnlinePlugin.php -->

```php
<?php declare(strict_types=1);

namespace MadelinePlugin\Danogentili;

use danog\MadelineProto\EventHandler\Attributes\Cron;
use danog\MadelineProto\EventHandler\Filter\FilterCommand;
use danog\MadelineProto\EventHandler\Message;
use danog\MadelineProto\EventHandler\SimpleFilter\FromAdmin;
use danog\MadelineProto\EventHandler\SimpleFilter\Incoming;
use danog\MadelineProto\PluginEventHandler;

final class OnlinePlugin extends PluginEventHandler
{
    private bool $isOnline = true;

    /**
     * Returns a list of names for properties that will be automatically saved to the session database (MySQL/postgres/redis if configured, the session file otherwise).
     */
    public function __sleep(): array
    {
        return ['isOnline'];
    }

    public function setOnline(bool $online): void
    {
        $this->isOnline = $online;
    }

    public function isPluginEnabled(): bool
    {
        // Only users can be online/offline
        return $this->getSelf()['bot'] === false;
    }

    #[Cron(period: 60.0)]
    public function cron(): void
    {
        $this->account->updateStatus(offline: !$this->isOnline);
    }

    #[FilterCommand('online')]
    public function toggleOnline(Incoming&Message&FromAdmin $message): void
    {
        $this->isOnline = true;
    }

    #[FilterCommand('offline')]
    public function toggleOffline(Incoming&Message&FromAdmin $message): void
    {
        $this->isOnline = false;
    }
}

```

<!-- cut_here_end examples/plugins/Danogentili/OnlinePlugin.php -->

And, to toggle the settings from the outside of the bot (for example using a helper bot, or another program):

```php
<?php

$online = true;
//$online = false;

$API = new \danog\MadelineProto\API('session.madeline');
$API->getEventHandler(\MadelinePlugin\Danogentili\OnlinePlugin::class)->setOnline($online);
```

#### Creating and uploading text files

Instead of writing to a file and then uploading it, you can use a `ReadableBuffer` to upload a file from a string, instead:

```php
use Amp\ReadableBuffer;

$contents = "Something";

$this->sendDocument(
    peer: 'danogentili',
    file: new ReadableBuffer($contents)
);
```

#### Logging

Instead of logging to separate files, you can use MadelineProto's built-in logger, which will write everything to `MadelineProto.log`:

```php
$this->logger("Some text");
```

You can also use the new `openFileAppendOnly` function, to open a file in write-only append-only mode in onStart and use it in your bot.  
You may also wrap the `File` resource returned by openFileAppendOnly in a proper PSR logger using [amphp/log](https://github.com/amphp/log).

```php
use danog\MadelineProto\SimpleEventHandler;
use danog\MadelineProto\Tools;
use Amp\Log\ConsoleFormatter;
use Amp\Log\StreamHandler;
use Monolog\Logger;

class MyEventHandler extends SimpleEventHandler {
    private Logger $customLogger;
    public function onStart()
    {
        // As documented in https://github.com/amphp/log
        $handler = new StreamHandler(Tools::openFileAppendOnly('file.log'));

        $this->customLogger = new Logger('main');
        $this->customLogger->pushHandler($handler);
    }

    public function someOtherMethod(): void {
        $this->customLogger->debug("Hello, world!");
        $this->customLogger->info("Hello, world!");
        $this->customLogger->notice("Hello, world!");
        $this->customLogger->error("Hello, world!");
        $this->customLogger->alert("Hello, world!");
    }
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

Webhooks will **greatly slow down your bot** if used directly inside of PHP code.  

**Only use the [event handler](#async-event-driven) when writing a MadelineProto bot**, because update handling in the **event handler** is completely parallelized and non-blocking.

Webhooks must **only** be used when consuming MadelineProto updates from another programming language, like for example **Javascript**.  

If your bot is written in PHP, [use the event handler, instead](https://docs.madelineproto.xyz/docs/UPDATES.html).  

```php
$MadelineProto = new \danog\MadelineProto\API('bot.madeline');

// NOT recommended when directly writing MadelineProto bots.
// ONLY use when exposing updates via an HTTP API to another language (like Javascript).

$MadelineProto->setWebhook('https://example.com');
```

## getUpdates

Only useful when consuming MadelineProto updates through an API in another language (like Javascript), **absolutely not recommended when directly writing MadelineProto bots**.  

`getUpdates` will **greatly slow down your bot** if used directly inside of PHP code.  

**Only use the [event handler](#async-event-driven) when writing a MadelineProto bot**, because update handling in the **event handler** is completely parallelized and non-blocking.

`getUpdates` must **only** be used when consuming MadelineProto updates from another programming language, like for example **Javascript**.  

If your bot is written in PHP, [use the event handler, instead](https://docs.madelineproto.xyz/docs/UPDATES.html).  

```php
$MadelineProto = new \danog\MadelineProto\API('bot.madeline');

// NOT recommended when directly writing MadelineProto bots.
// ONLY use when exposing updates via an HTTP API to another language (like Javascript).

// DO NOT use this to handle updates in PHP code, it will cause crashes.

// Same parameters as for bot API getUpdates
echo json_encode($MadelineProto->getUpdates($_GET));
```

<a href="https://docs.madelineproto.xyz/docs/FILTERS.html">Next section</a>