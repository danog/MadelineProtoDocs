---
title: channels.getLeftChannels
description: Get a list of [channels/supergroups](https://core.telegram.org/api/channel) we left
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: channels.getLeftChannels  
[Back to methods index](index.md)


Get a list of [channels/supergroups](https://core.telegram.org/api/channel) we left

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|offset|[int](../types/int.md) | Offset for [pagination](https://core.telegram.org/api/offsets) | Yes|


### Return type: [messages\_Chats](../types/messages_Chats.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$messages_Chats = $MadelineProto->channels->getLeftChannels(['offset' => int, ]);
```

Or, if you're into Lua:

```lua
messages_Chats = channels.getLeftChannels({offset=int, })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|403|TAKEOUT_REQUIRED|A takeout session has to be initialized, first|


