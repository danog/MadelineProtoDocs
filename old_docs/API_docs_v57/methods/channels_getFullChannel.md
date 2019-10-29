---
title: channels.getFullChannel
description: You cannot use this method directly, use the get_pwr_chat, get_info, get_full_info methods instead (see https://docs.madelineproto.xyz for more info)
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: channels.getFullChannel  
[Back to methods index](index.md)


You cannot use this method directly, use the get_pwr_chat, get_info, get_full_info methods instead (see https://docs.madelineproto.xyz for more info)

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|channel|[Username, chat ID, Update, Message or InputChannel](../types/InputChannel.md) | You cannot use this method directly, use the get_pwr_chat, get_info, get_full_info methods instead (see https://docs.madelineproto.xyz for more info) | Optional|


### Return type: [messages\_ChatFull](../types/messages_ChatFull.md)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$messages_ChatFull = $MadelineProto->channels->getFullChannel(['channel' => InputChannel, ]);
```

Or, if you're into Lua:

```lua
messages_ChatFull = channels.getFullChannel({channel=InputChannel, })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|CHANNEL_INVALID|The provided channel is invalid|
|400|CHANNEL_PRIVATE|You haven't joined this channel/supergroup|
|400|MSG_ID_INVALID|Invalid message ID provided|
|403|CHANNEL_PUBLIC_GROUP_NA|channel/supergroup not available|
|-503|Timeout|Timeout while fetching data|


