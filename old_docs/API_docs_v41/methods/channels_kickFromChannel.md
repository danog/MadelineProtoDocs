---
title: channels.kickFromChannel
description: Kick user from channel
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: channels.kickFromChannel  
[Back to methods index](index.md)


Kick user from channel

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|channel|[Username, chat ID, Update, Message or InputChannel](../types/InputChannel.md) | The channel | Optional|
|user\_id|[Username, chat ID, Update, Message or InputUser](../types/InputUser.md) | The user to kick | Optional|
|kicked|[Bool](../types/Bool.md) | Kick or unkick? | Yes|


### Return type: [Updates](../types/Updates.md)

### Can bots use this method: **YES**


### MadelineProto Example:


```
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Updates = $MadelineProto->channels->kickFromChannel(['channel' => InputChannel, 'user_id' => InputUser, 'kicked' => Bool, ]);
```

### [PWRTelegram HTTP API](https://pwrtelegram.xyz) example (NOT FOR MadelineProto):

### As a bot:

POST/GET to `https://api.pwrtelegram.xyz/botTOKEN/madeline`

Parameters:

* method - channels.kickFromChannel
* params - `{"channel": InputChannel, "user_id": InputUser, "kicked": Bool, }`



### As a user:

POST/GET to `https://api.pwrtelegram.xyz/userTOKEN/channels.kickFromChannel`

Parameters:

channel - Json encoded InputChannel

user_id - Json encoded InputUser

kicked - Json encoded Bool




Or, if you're into Lua:

```
Updates = channels.kickFromChannel({channel=InputChannel, user_id=InputUser, kicked=Bool, })
```

