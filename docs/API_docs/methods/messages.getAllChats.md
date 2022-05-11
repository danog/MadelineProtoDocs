---
title: "messages.getAllChats"
description: "Get all chats, channels and supergroups"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_getAllChats.html
---
# Method: messages.getAllChats
[Back to methods index](index.html)



Get all chats, channels and supergroups

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|except\_ids|Array of [long](/API_docs/types/long.html) | Except these chats/channels/supergroups | Yes|


### Return type: [messages.Chats](/API_docs/types/messages.Chats.html)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

// PHP 8+ syntax, use an array on PHP 7.
$messages_Chats = $MadelineProto->messages->getAllChats(except_ids: [long, long], );
```

