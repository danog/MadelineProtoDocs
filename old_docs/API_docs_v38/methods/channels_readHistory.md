---
title: channels.readHistory
description: Mark channel/supergroup history as read
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: channels.readHistory  
[Back to methods index](index.md)


Mark channel/supergroup history as read

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|channel|[Username, chat ID, Update, Message or InputChannel](../types/InputChannel.md) | The channel/supergroup | Optional|
|max\_id|[int](../types/int.md) | Maximum message ID to mark as read | Yes|


### Return type: [Bool](../types/Bool.md)

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

$Bool = $MadelineProto->channels->readHistory(['channel' => InputChannel, 'max_id' => int, ]);
```

### [PWRTelegram HTTP API](https://pwrtelegram.xyz) example (NOT FOR MadelineProto):



### As a user:

POST/GET to `https://api.pwrtelegram.xyz/userTOKEN/channels.readHistory`

Parameters:

channel - Json encoded InputChannel

max_id - Json encoded int




Or, if you're into Lua:

```lua
Bool = channels.readHistory({channel=InputChannel, max_id=int, })
```

### Errors this method can return:

| Error    | Description   |
|----------|---------------|
|CHANNEL_INVALID|The provided channel is invalid|
|CHANNEL_PRIVATE|You haven't joined this channel/supergroup|


