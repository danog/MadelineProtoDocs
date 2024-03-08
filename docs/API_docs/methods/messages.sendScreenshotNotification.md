---
title: "messages.sendScreenshotNotification"
description: "Notify the other user in a private chat that a screenshot of the chat was taken"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_sendScreenshotNotification.html
---
# Method: messages.sendScreenshotNotification
[Back to methods index](index.html)



Notify the other user in a private chat that a screenshot of the chat was taken

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Other user | Optional|
|reply\_to|[InputReplyTo](/API_docs/types/InputReplyTo.html) | Indicates the message that was screenshotted (the specified message ID can also be `0` to avoid indicating any specific message). | Yes|


### Return type: [Updates](/API_docs/types/Updates.html)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Updates = $MadelineProto->messages->sendScreenshotNotification(peer: $InputPeer, reply_to: $InputReplyTo, );
```

