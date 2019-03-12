---
title: messages.sendScreenshotNotification
description: Send screenshot notification
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: messages.sendScreenshotNotification  
[Back to methods index](index.md)


Send screenshot notification

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[Username, chat ID, Update, Message or InputPeer](../types/InputPeer.md) | Where to send the notification | Optional|
|reply\_to\_msg\_id|[int](../types/int.md) | Reply to message by ID | Yes|


### Return type: [Updates](../types/Updates.md)

### Can bots use this method: **NO**


### MadelineProto Example:


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
define('MADELINE_BRANCH', '');
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Updates = $MadelineProto->messages->sendScreenshotNotification(['peer' => InputPeer, 'reply_to_msg_id' => int, ]);
```

### [PWRTelegram HTTP API](https://pwrtelegram.xyz) example (NOT FOR MadelineProto):



### As a user:

POST/GET to `https://api.pwrtelegram.xyz/userTOKEN/messages.sendScreenshotNotification`

Parameters:

peer - Json encoded InputPeer

reply_to_msg_id - Json encoded int




Or, if you're into Lua:

```lua
Updates = messages.sendScreenshotNotification({peer=InputPeer, reply_to_msg_id=int, })
```

### Errors this method can return:

| Error    | Description   |
|----------|---------------|
|PEER_ID_INVALID|The provided peer id is invalid|


