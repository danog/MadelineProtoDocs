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
|reply\_to\_msg\_id|[int](/API_docs/types/int.html) | ID of message that was screenshotted, can be 0 | Yes|


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

// PHP 8+ syntax, use an array on PHP 7.
$Updates = $MadelineProto->messages->sendScreenshotNotification(peer: InputPeer, reply_to_msg_id: int, );
```

