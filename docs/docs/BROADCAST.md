---
title: "Broadcasting messages to all users"
description: "MadelineProto can be used to broadcast messages to all users, chats and channels of a bot or userbot.  "
nav_order: 9
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Broadcasting messages to all users

MadelineProto can be used to broadcast messages to all users, chats and channels of a bot or userbot.  

Note that **unlike the bot API**, MadelineProto **can** be used to fetch the full list of users, chats and channels of a normal bot, simply using its bot token.  

## Broadcast API

MadelineProto offers a simple broadcast API, that can be used to asynchronously broadcast messages to all users of a bot or userbot in the background, without incurring in timeouts or other issues.  

See [here &raquo;](https://github.com/danog/MadelineProto/blob/v8/examples/bot.php) for a full example of the broadcast API.  

### Forward messages

Use `broadcastForwardMessages` to forward a list of messages to all peers (users, chats, channels) of the bot.  

It will return an integer ID that can be used to:

- Get the current broadcast progress with [getBroadcastProgress](#get-progress)
- Cancel the broadcast using [cancelBroadcast](#cancel-a-broadcast)

Note that to avoid manually polling the progress, MadelineProto will also periodically emit [updateBroadcastProgress updates](#get-progress), containing a Progress object for all broadcasts currently in-progress.

```php
<?php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('bot.madeline');

// Works OK with both bots and userbots
$MadelineProto->start();

// Send messages, showing the "Forwarded from" header
$id = $MadelineProto->broadcastForwardMessages(
    from_peer: 101374607,
    ids: [1, 2, 3, 4],
    drop_author: false,
);

// Send messages WITHOUT showing the "Forwarded from" header
$id = $MadelineProto->broadcastForwardMessages(
    from_peer: 101374607,
    ids: [1, 2, 3, 4],
    drop_author: true,
);
```

An optional `filter` parameter can also be used, specifying a [peer filter](#filtering).  

### Send messages

Use `broadcastMessages` to broadcast a list of messages to all peers (users, chats, channels) of the bot.  

A simplified version of this method is also available: [broadcastForwardMessages](#forward-messages) can work with pre-prepared messages.  

It will return an integer ID that can be used to:

- Get the current broadcast progress with [getBroadcastProgress](#get-progress)
- Cancel the broadcast using [cancelBroadcast](#cancel-a-broadcast)

Note that to avoid manually polling the progress, MadelineProto will also periodically emit [updateBroadcastProgress updates](#get-progress), containing a Progress object for all broadcasts currently in-progress.

```php
<?php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('bot.madeline');

// Works OK with both bots and userbots
$MadelineProto->start();

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

It will return an integer ID that can be used to:

- Get the current broadcast progress with [getBroadcastProgress](#get-progress)
- Cancel the broadcast using [cancelBroadcast](#cancel-a-broadcast)

Note that to avoid manually polling the progress, MadelineProto will also periodically emit [updateBroadcastProgress updates](#get-progress), containing a Progress object for all broadcasts currently in-progress.

An optional `filter` parameter can also be used, specifying a [peer filter](#filtering).  

### Filtering

### Cancel a broadcast

Use `cancelBroadcast` to a cancel an in-progress broadcast.

### Get progress

You can use `getBroadcastProgress` to get the progress of a currently running broadcast.
The method return null if the broadcast doesn't exist, has already completed or was cancelled.  

Use updateBroadcastProgress updates to get real-time progress status without polling.

<a href="https://docs.madelineproto.xyz/docs/UPDATES.html">Next section</a>