---
title: "messages.getChats"
description: "Returns chat basic info on their IDs."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_getChats.html
---
# Method: messages.getChats
[Back to methods index](index.html)



Returns chat basic info on their IDs.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|id|Array of [long](/API_docs/types/long.html) | List of chat IDs | Yes|


### Return type: [messages.Chats](/API_docs/types/messages.Chats.html)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

// PHP 8+ syntax, use an array on PHP 7.
$messages_Chats = $MadelineProto->messages->getChats(id: [long, long], );
```

