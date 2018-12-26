---
title: channels.updatePinnedMessage
description: Set the pinned message of a channel/supergroup
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: channels.updatePinnedMessage  
[Back to methods index](index.md)


Set the pinned message of a channel/supergroup

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|silent|[Bool](../types/Bool.md) | Pin silently | Optional|
|channel|[Username, chat ID, Update, Message or InputChannel](../types/InputChannel.md) | The channel/supergroup | Optional|
|id|[int](../types/int.md) | The ID of the message to pin | Yes|


### Return type: [Updates](../types/Updates.md)

### Can bots use this method: **YES**


### MadelineProto Example:


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Updates = $MadelineProto->channels->updatePinnedMessage(['silent' => Bool, 'channel' => InputChannel, 'id' => int, ]);
```

### [PWRTelegram HTTP API](https://pwrtelegram.xyz) example (NOT FOR MadelineProto):

### As a bot:

POST/GET to `https://api.pwrtelegram.xyz/botTOKEN/madeline`

Parameters:

* method - channels.updatePinnedMessage
* params - `{"silent": Bool, "channel": InputChannel, "id": int, }`



### As a user:

POST/GET to `https://api.pwrtelegram.xyz/userTOKEN/channels.updatePinnedMessage`

Parameters:

silent - Json encoded Bool

channel - Json encoded InputChannel

id - Json encoded int




Or, if you're into Lua:

```lua
Updates = channels.updatePinnedMessage({silent=Bool, channel=InputChannel, id=int, })
```

### Errors this method can return:

| Error    | Description   |
|----------|---------------|
|CHANNEL_INVALID|The provided channel is invalid|
|CHAT_ADMIN_REQUIRED|You must be an admin in this chat to do this|
|CHAT_ID_INVALID|The provided chat id is invalid|
|CHAT_NOT_MODIFIED|The pinned message wasn't modified|


