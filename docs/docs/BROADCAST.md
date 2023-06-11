---
title: "Broadcasting messages to all users"
description: "MadelineProto can be used to broadcast messages to all users, chats and channels of a bot or userbot.  "
nav_order: 10
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Broadcasting messages to all users

MadelineProto can be used to broadcast messages to all users, chats and channels of a bot or userbot.  

Note that unlike the bot API, MadelineProto can be used to fetch the full list of users, chats and channels of a **normal bot, simply using its bot token**.  

**All** users, chats and channels of the bot will be fetched, **regardless** of their last activity date: for example, if you just logged in with a bot token in MadelineProto 5 minutes ago, MadelineProto will fetch **all** users, chats and channels, even if their last activity is 5+ years ago!  

## Broadcast API

MadelineProto offers a simple broadcast API, that can be used to asynchronously broadcast messages to all users of a bot or userbot in the background, without incurring in timeouts or other issues.  

See [here &raquo;](https://github.com/danog/MadelineProto/blob/v8/examples/bot.php) for a full example of the broadcast API.  

### Forward messages

Use `broadcastForwardMessages` to forward a list of messages to all peers (users, chats, channels) of the bot.  

This method will automatically handle rate limits, waiting to ensure all messages are sent correctly.  

It will return an integer ID that can be used to:

- Get the current broadcast progress with [getBroadcastProgress](#get-progress)
- Cancel the broadcast using [cancelBroadcast](#cancel-a-broadcast)

Note that to avoid manually polling the progress, MadelineProto will also periodically emit [updateBroadcastProgress updates](#get-progress), containing a Progress object for all broadcasts currently in-progress.  
Note that the process may take even hours to start, so be patient.  

```php
<?php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('bot.madeline');

// Works OK with both bots and userbots
$MadelineProto->start();

// Or, instead of start() you can use botLogin (bots only)
//$MadelineProto->botLogin('1234:token');

// Let's forward two messages from the @MadelineProto channel!
// Channel ID: @MadelineProto
// Message ID 1: 614
// Message ID 2: 613
// Link 1: https://t.me/MadelineProto/613
// Link 2: https://t.me/MadelineProto/614

$from_peer = '@MadelineProto'; // Can also be a numeric bot API ID
$message_ids = [613, 614];

// Send messages, showing the "Forwarded from" header
$id = $MadelineProto->broadcastForwardMessages(
    from_peer: $from_peer,
    message_ids: $message_ids,
    drop_author: false,
);

// Send messages WITHOUT showing the "Forwarded from" header
$id = $MadelineProto->broadcastForwardMessages(
    from_peer: $from_peer,
    message_ids: $message_ids,
    drop_author: true,
);
```

An optional `filter` parameter can also be used, specifying a [peer filter](#filtering).  

### Send messages

Use `broadcastMessages` to broadcast a list of messages to all peers (users, chats, channels) of the bot.  

This method will automatically handle rate limits, waiting to ensure all messages are sent correctly.  

A simplified version of this method is also available: [broadcastForwardMessages](#forward-messages) can work with pre-prepared messages.  

It will return an integer ID that can be used to:

- Get the current broadcast progress with [getBroadcastProgress](#get-progress)
- Cancel the broadcast using [cancelBroadcast](#cancel-a-broadcast)

Note that to avoid manually polling the progress, MadelineProto will also periodically emit [updateBroadcastProgress updates](#get-progress), containing a Progress object for all broadcasts currently in-progress.  
Note that the process may take even hours to start, so be patient.  

```php
<?php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('bot.madeline');

// Works OK with both bots and userbots
$MadelineProto->start();

// Or, instead of start() you can use botLogin (bots only)
//$MadelineProto->botLogin('1234:token');

$id = $MadelineProto->broadcastMessages([
    ['message' => 'This broadcast is powered by @MadelineProto!'],
    ['message' => 'This media broadcast is powered by @MadelineProto!', 'media' => [
        '_' => 'inputMediaUploadedPhoto',
        'file' => 'https://docs.madelineproto.xyz/logo-hover.png'
    ]],
]);
```

An optional `filter` parameter can also be used, specifying a [peer filter](#filtering).  

### Custom action

Use `broadcastCustom` to execute a custom broadcast action with all peers (users, chats, channels) of the bot.  

This method will **NOT** automatically handle rate limits.  
To handle rate limits and errors automatically, a simplified version of this method is available, [broadcastForwardMessages &raquo;](#forward-messages) and [broadcastMessages &raquo;](#send-messages).  

It will return an integer ID that can be used to:

- Get the current broadcast progress with [getBroadcastProgress](#get-progress)
- Cancel the broadcast using [cancelBroadcast](#cancel-a-broadcast)

Note that to avoid manually polling the progress, MadelineProto will also periodically emit [updateBroadcastProgress updates](#get-progress), containing a Progress object for all broadcasts currently in-progress.

An optional `filter` parameter can also be used, specifying a [peer filter](#filtering).  
Note that the process may take even hours to start, so be patient.  

```php
<?php

use danog\MadelineProto\API;
use danog\MadelineProto\Broadcast\Action;
use danog\MadelineProto\RPCErrorException;
use Amp\Cancellation;

// This class MUST be autoloadable via composer
final class CustomBroadcastAction implements Action {
    public function __construct(private API $API, private string $message) {}
    public function act(int $broadcastId, int $peer, Cancellation $cancellation): void
    {
        try {
            if ($cancellation->isRequested()) {
                return;
            }
            $this->API->messages->sendMessage(
                peer: $peer,
                message: $this->message,
            );
        } catch (RPCErrorException $e) {
            if ($e->rpc === 'INPUT_USER_DEACTIVATED') {
                return;
            }
            if ($e->rpc === 'USER_IS_BOT') {
                return;
            }
            if ($e->rpc === 'CHAT_WRITE_FORBIDDEN') {
                return;
            }
            if ($e->rpc === 'USER_IS_BLOCKED') {
                return;
            }
            if ($e->rpc === 'PEER_ID_INVALID') {
                return;
            }
            throw $e;
        }
    }
}

// In some other file...
$id = $MadelineProto->broadcastCustom(new CustomBroadcastAction($MadelineProto, 'This broadcast is powered by @MadelineProto!'));
```

### Filtering

All broadcast methods allow specifying a custom peer filter:

```php
<?php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

use danog\MadelineProto\API;
use danog\MadelineProto\Broadcast\Filter;

$MadelineProto = new API('bot.madeline');

// Works OK with both bots and userbots
$MadelineProto->start();

// Or, instead of start() you can use botLogin (bots only)
//$MadelineProto->botLogin('1234:token');

// Send messages, showing the "Forwarded from" header
$id = $MadelineProto->broadcastForwardMessages(
    from_peer: 101374607,
    ids: [1, 2, 3, 4],
    drop_author: false,
    filter: new Filter(
        allowUsers: true,
        allowBots: false,
        allowGroups: true,
        allowChannels: false,
        blacklist: [], // Optional
        whitelist: null // Optional array, if null all IDs are allowed (equivalent to *)
    )
);
```

### Cancel a broadcast

Use `cancelBroadcast` to a cancel an in-progress broadcast.

```php
$MadelineProto->cancelBroadcast(123);
```

### Get progress

```php
use danog\MadelineProto\Broadcast\Progress;
use danog\MadelineProto\Broadcast\Status;

$progress = $MadelineProto->getBroadcastProgress(123);

if ($progress !== null) {
    assert($progress instanceof Progress);

    $progressStr = (string) $progress;
    echo "Human-readable progress: $progressStr".PHP_EOL;

    // 123
    $broadcastId = $progress->broadcastId;

    // One of Status::GATHERING_PEERS, Status::BROADCASTING, Status::FINISHED, Status::CANCELLED
    $status = $progress->status;

    $pendingCount = $progress->pendingCount;
    $sucessCount = $progress->successCount;
    $sucessCount = $progress->failCount;
}
```

You can use `getBroadcastProgress` to get the progress of a currently running broadcast.
The method return null if the broadcast doesn't exist, has already completed or was cancelled.  

Use updateBroadcastProgress updates to get real-time progress status without polling, [here's a full example &raquo;](https://github.com/danog/MadelineProto/blob/v8/examples/bot.php).  

<a href="https://docs.madelineproto.xyz/docs/UPDATES.html">Next section</a>