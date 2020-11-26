---
title: channels.readMessageContents
description: Mark [channel/supergroup](https://core.telegram.org/api/channel) message contents as read
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/channels_readMessageContents.html
---
# Method: channels.readMessageContents
[Back to methods index](index.md)



Mark [channel/supergroup](https://core.telegram.org/api/channel) message contents as read

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|channel|[Username, chat ID, Update, Message or InputChannel](../types/InputChannel.md) | [Channel/supergroup](https://core.telegram.org/api/channel) | Optional|
|id|Array of [int](../types/int.md) | IDs of messages whose contents should be marked as read | Yes|


### Return type: [Bool](../types/Bool.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$Bool = $MadelineProto->channels->readMessageContents(['channel' => InputChannel, 'id' => [int, int], ]);
```

Or, if you're into Lua:

```lua
Bool = channels.readMessageContents({channel=InputChannel, id={int}, })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|CHANNEL_INVALID|The provided channel is invalid|
|400|CHANNEL_PRIVATE|You haven't joined this channel/supergroup|
|400|MSG_ID_INVALID|Invalid message ID provided|
|-503|Timeout|Timeout while fetching data|


