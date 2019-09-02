---
title: updates.getChannelDifference
description: You cannot use this method directly, see https://docs.madelineproto.xyz for more info on handling updates
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: updates.getChannelDifference  
[Back to methods index](index.md)


You cannot use this method directly, see https://docs.madelineproto.xyz for more info on handling updates

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|channel|[Username, chat ID, Update, Message or InputChannel](../types/InputChannel.md) | You cannot use this method directly, see https://docs.madelineproto.xyz for more info on handling updates | Optional|
|filter|[ChannelMessagesFilter](../types/ChannelMessagesFilter.md) | You cannot use this method directly, see https://docs.madelineproto.xyz for more info on handling updates | Optional|
|pts|[int](../types/int.md) | You cannot use this method directly, see https://docs.madelineproto.xyz for more info on handling updates | Yes|
|limit|[int](../types/int.md) | You cannot use this method directly, see https://docs.madelineproto.xyz for more info on handling updates | Yes|


### Return type: [updates\_ChannelDifference](../types/updates_ChannelDifference.md)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$updates_ChannelDifference = $MadelineProto->updates->getChannelDifference(['channel' => InputChannel, 'filter' => ChannelMessagesFilter, 'pts' => int, 'limit' => int, ]);
```

Or, if you're into Lua:

```lua
updates_ChannelDifference = updates.getChannelDifference({channel=InputChannel, filter=ChannelMessagesFilter, pts=int, limit=int, })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|CHANNEL_INVALID|The provided channel is invalid|
|400|CHANNEL_PRIVATE|You haven't joined this channel/supergroup|
|400|PERSISTENT_TIMESTAMP_EMPTY|Persistent timestamp empty|
|400|PERSISTENT_TIMESTAMP_INVALID|Persistent timestamp invalid|
|400|RANGES_INVALID|Invalid range provided|
|406|AUTH_KEY_DUPLICATED|An auth key with the same ID was already generated|
|403|CHANNEL_PUBLIC_GROUP_NA|channel/supergroup not available|
|-503|Timeout|Timeout while fetching data|


