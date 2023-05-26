---
title: "Broadcasting messages to all users"
description: "MadelineProto can be used to broadcast messages to all users, chats and channels of a bot or userbot.  "
nav_order: 9
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Broadcasting messages to all users

MadelineProto can be used to broadcast messages to all users, chats and channels of a bot or userbot.  

Note that **unlike the bot API**, MadelineProto **can** be used to fetch the full list of users, chats and channels of a normal bot, simply using its bot token.  

## Fetching the member list

To fetch the full list of users, chats and channels of a bot or userbot, use this code:

Bots only:

```php
<?php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('bot.madeline');
$MadelineProto->botLogin('123456:token');

var_dump($MadelineProto->getDialogIds());
```

Bots/userbots:

```php
<?php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('bot.madeline');
$MadelineProto->start();

var_dump($MadelineProto->getDialogIds());
```

`getDialogIds` will return a list of bot API IDs,containing the full list of users, chats and channels accessible by the bot, that may then be used to send messages or execute other action.  

*Note*: `getDialogIds` may take a **long time** to fetch the full list.  
To avoid timeouts, use the [broadcast API &raquo;](#broadcast-api), instead.  

## Broadcast API

MadelineProto offers a simple broadcast API, that can be used to asynchronously broadcast messages to all users of a bot or userbot in the background, without incurring in timeouts or other issues.  

### Messages

Use `broadcastMessages` to broadcast messages.

<a href="https://docs.madelineproto.xyz/docs/UPDATES.html">Next section</a>