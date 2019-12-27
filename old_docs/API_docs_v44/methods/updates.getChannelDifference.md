---
title: updates.getChannelDifference
description: You cannot use this method directly, see https://docs.madelineproto.xyz for more info on handling updates
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/updates_getChannelDifference.html
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


### Return type: [updates.ChannelDifference](../types/updates.ChannelDifference.md)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$updates.ChannelDifference = $MadelineProto->updates->getChannelDifference(['channel' => InputChannel, 'filter' => ChannelMessagesFilter, 'pts' => int, 'limit' => int, ]);
```

Or, if you're into Lua:

```lua
updates.ChannelDifference = updates.getChannelDifference({channel=InputChannel, filter=ChannelMessagesFilter, pts=int, limit=int, })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|CHANNEL_INVALID|The provided channel is invalid|
|400|CHANNEL_PRIVATE|You haven't joined this channel/supergroup|
|400|FROM_MESSAGE_BOT_DISABLED|Bots can't use fromMessage min constructors|
|400|MSG_ID_INVALID|Invalid message ID provided|
|400|PERSISTENT_TIMESTAMP_EMPTY|Persistent timestamp empty|
|400|PERSISTENT_TIMESTAMP_INVALID|Persistent timestamp invalid|
|400|PINNED_DIALOGS_TOO_MUCH|Too many pinned dialogs|
|400|RANGES_INVALID|Invalid range provided|
|406|AUTH_KEY_DUPLICATED|An auth key with the same ID was already generated|
|403|CHANNEL_PUBLIC_GROUP_NA|channel/supergroup not available|
|-503|Timeout|Timeout while fetching data|


