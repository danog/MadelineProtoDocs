---
title: channels.updateUsername
description: Update the username of a supergroup/channel
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: channels.updateUsername  
[Back to methods index](index.md)


Update the username of a supergroup/channel

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|channel|[Username, chat ID, Update, Message or InputChannel](../types/InputChannel.md) | The channel/supergroup | Optional|
|username|[string](../types/string.md) | The new username | Yes|


### Return type: [Bool](../types/Bool.md)

### Can bots use this method: **NO**


### MadelineProto Example:


```
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Bool = $MadelineProto->channels->updateUsername(['channel' => InputChannel, 'username' => 'string', ]);
```

### [PWRTelegram HTTP API](https://pwrtelegram.xyz) example (NOT FOR MadelineProto):



### As a user:

POST/GET to `https://api.pwrtelegram.xyz/userTOKEN/channels.updateUsername`

Parameters:

channel - Json encoded InputChannel

username - Json encoded string




Or, if you're into Lua:

```
Bool = channels.updateUsername({channel=InputChannel, username='string', })
```

### Errors this method can return:

| Error    | Description   |
|----------|---------------|
|CHANNEL_INVALID|The provided channel is invalid|
|CHANNELS_ADMIN_PUBLIC_TOO_MUCH|You're admin of too many public channels, make some channels private to change the username of this channel|
|CHAT_ADMIN_REQUIRED|You must be an admin in this chat to do this|
|USERNAME_INVALID|The provided username is not valid|
|USERNAME_OCCUPIED|The provided username is already occupied|


