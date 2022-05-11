---
title: "messages.updatePinnedMessage"
description: "Pin a message"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_updatePinnedMessage.html
---
# Method: messages.updatePinnedMessage
[Back to methods index](index.html)



Pin a message

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|silent|[Bool](/API_docs/types/Bool.html) | Pin the message silently, without triggering a notification | Optional|
|unpin|[Bool](/API_docs/types/Bool.html) | Whether the message should unpinned or pinned | Optional|
|pm\_oneside|[Bool](/API_docs/types/Bool.html) | Whether the message should only be pinned on the local side of a one-to-one chat | Optional|
|peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | The peer where to pin the message | Optional|
|id|[int](/API_docs/types/int.html) | The message to pin or unpin | Yes|


### Return type: [Updates](/API_docs/types/Updates.html)

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
$Updates = $MadelineProto->messages->updatePinnedMessage(silent: Bool, unpin: Bool, pm_oneside: Bool, peer: InputPeer, id: int, );
```

