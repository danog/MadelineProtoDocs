---
title: channels.exportMessageLink
description: Get the link of a message in a channel
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: channels.exportMessageLink  
[Back to methods index](index.md)


Get the link of a message in a channel

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|channel|[Username, chat ID, Update, Message or InputChannel](../types/InputChannel.md) | The channel/supergroup | Optional|
|id|[int](../types/int.md) | The ID of the message | Yes|


### Return type: [ExportedMessageLink](../types/ExportedMessageLink.md)

### Can bots use this method: **NO**


### MadelineProto Example:


```
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$ExportedMessageLink = $MadelineProto->channels->exportMessageLink(['channel' => InputChannel, 'id' => int, ]);
```

### [PWRTelegram HTTP API](https://pwrtelegram.xyz) example (NOT FOR MadelineProto):



### As a user:

POST/GET to `https://api.pwrtelegram.xyz/userTOKEN/channels.exportMessageLink`

Parameters:

channel - Json encoded InputChannel

id - Json encoded int




Or, if you're into Lua:

```
ExportedMessageLink = channels.exportMessageLink({channel=InputChannel, id=int, })
```

### Errors this method can return:

| Error    | Description   |
|----------|---------------|
|CHANNEL_INVALID|The provided channel is invalid|


