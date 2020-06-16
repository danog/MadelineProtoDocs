---
title: channels.getFullChannel
description: Get full info about a channel
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/channels_getFullChannel.html
---
# Method: channels.getFullChannel
[Back to methods index](index.md)



Get full info about a channel

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|channel|[Username, chat ID, Update, Message or InputChannel](../types/InputChannel.md) | The channel to get info about | Optional|


### Return type: [messages.ChatFull](../types/messages.ChatFull.md)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$messages.ChatFull = $MadelineProto->channels->getFullChannel(['channel' => InputChannel, ]);
```

Or, if you're into Lua:

```lua
messages.ChatFull = channels.getFullChannel({channel=InputChannel, })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|CHANNEL_INVALID|The provided channel is invalid|
|400|CHANNEL_PRIVATE|You haven't joined this channel/supergroup|
|400|MSG_ID_INVALID|Invalid message ID provided|
|406|AUTH_KEY_DUPLICATED|An auth key with the same ID was already generated|
|403|CHANNEL_PUBLIC_GROUP_NA|channel/supergroup not available|
|-503|Timeout|Timeout while fetching data|


