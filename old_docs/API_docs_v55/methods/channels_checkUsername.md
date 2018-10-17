---
title: channels.checkUsername
description: Check if this username is free and can be assigned to a channel/supergroup
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: channels.checkUsername  
[Back to methods index](index.md)


Check if this username is free and can be assigned to a channel/supergroup

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|channel|[Username, chat ID, Update, Message or InputChannel](../types/InputChannel.md) | The channel/supergroup | Optional|
|username|[string](../types/string.md) | The new username for this channel/supergroup | Yes|


### Return type: [Bool](../types/Bool.md)

### Can bots use this method: **NO**


### MadelineProto Example:


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Bool = $MadelineProto->channels->checkUsername(['channel' => InputChannel, 'username' => 'string', ]);
```

### [PWRTelegram HTTP API](https://pwrtelegram.xyz) example (NOT FOR MadelineProto):



### As a user:

POST/GET to `https://api.pwrtelegram.xyz/userTOKEN/channels.checkUsername`

Parameters:

channel - Json encoded InputChannel

username - Json encoded string




Or, if you're into Lua:

```lua
Bool = channels.checkUsername({channel=InputChannel, username='string', })
```

### Errors this method can return:

| Error    | Description   |
|----------|---------------|
|CHANNEL_INVALID|The provided channel is invalid|
|CHAT_ID_INVALID|The provided chat id is invalid|
|USERNAME_INVALID|The provided username is not valid|


