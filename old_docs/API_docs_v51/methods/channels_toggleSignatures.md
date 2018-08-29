---
title: channels.toggleSignatures
description: Toggle channel signatures
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: channels.toggleSignatures  
[Back to methods index](index.md)


Toggle channel signatures

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|channel|[Username, chat ID, Update, Message or InputChannel](../types/InputChannel.md) | The channel/supergroup | Optional|
|enabled|[Bool](../types/Bool.md) | Enable or disable channel signatures? | Yes|


### Return type: [Updates](../types/Updates.md)

### Can bots use this method: **NO**


### MadelineProto Example:


```
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Updates = $MadelineProto->channels->toggleSignatures(['channel' => InputChannel, 'enabled' => Bool, ]);
```

### [PWRTelegram HTTP API](https://pwrtelegram.xyz) example (NOT FOR MadelineProto):



### As a user:

POST/GET to `https://api.pwrtelegram.xyz/userTOKEN/channels.toggleSignatures`

Parameters:

channel - Json encoded InputChannel

enabled - Json encoded Bool




Or, if you're into Lua:

```
Updates = channels.toggleSignatures({channel=InputChannel, enabled=Bool, })
```

### Errors this method can return:

| Error    | Description   |
|----------|---------------|
|CHANNEL_INVALID|The provided channel is invalid|


