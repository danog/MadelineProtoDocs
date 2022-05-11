---
title: "messages.getMessages"
description: "Returns the list of messages by their IDs."
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_getMessages.html
---
# Method: messages.getMessages
[Back to methods index](index.html)



Returns the list of messages by their IDs.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|id|Array of [Message ID or InputMessage](/API_docs/types/InputMessage.html) | Message ID list | Yes|


### Return type: [messages.Messages](/API_docs/types/messages.Messages.html)

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
$messages_Messages = $MadelineProto->messages->getMessages(id: [InputMessage, InputMessage], );
```

