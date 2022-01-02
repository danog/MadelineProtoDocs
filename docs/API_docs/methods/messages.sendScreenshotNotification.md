---
title: "messages.sendScreenshotNotification"
description: "Notify the other user in a private chat that a screenshot of the chat was taken"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_sendScreenshotNotification.html
---
# Method: messages.sendScreenshotNotification
[Back to methods index](index.md)



Notify the other user in a private chat that a screenshot of the chat was taken

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](../types/InputPeer.md) | Other user | Optional|
|reply\_to\_msg\_id|[int](../types/int.md) | ID of message that was screenshotted, can be 0 | Yes|


### Return type: [Updates](../types/Updates.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Updates = $MadelineProto->messages->sendScreenshotNotification(['peer' => InputPeer, 'reply_to_msg_id' => int, ]);
```

Or, if you're into Lua:

```lua
Updates = messages.sendScreenshotNotification({peer=InputPeer, reply_to_msg_id=int, })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|PEER_ID_INVALID|The provided peer id is invalid|
|400|YOU_BLOCKED_USER|You blocked this user|


