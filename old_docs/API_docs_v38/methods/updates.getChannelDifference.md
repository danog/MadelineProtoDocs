---
title: updates.getChannelDifference
description: Returns the difference between the current state of updates of a certain channel and transmitted.
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/updates_getChannelDifference.html
---
# Method: updates.getChannelDifference
[Back to methods index](index.md)



Returns the difference between the current state of updates of a certain channel and transmitted.

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|force|[Bool](../types/Bool.md) | Set to true to skip some possibly unneeded updates and reduce server-side load | Optional|
|channel|[Username, chat ID, Update, Message or InputChannel](../types/InputChannel.md) | The channel | Optional|
|filter|[ChannelMessagesFilter](../types/ChannelMessagesFilter.md) | Messsage filter | Optional|
|pts|[int](../types/int.md) | Persistent timestamp (see [updates](https://core.telegram.org/api/updates)) | Yes|
|limit|[int](../types/int.md) | How many updates to fetch, max `100000`<br>Ordinary (non-bot) users are supposed to pass `10-100` | Yes|


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

$updates.ChannelDifference = $MadelineProto->updates->getChannelDifference(['force' => Bool, 'channel' => InputChannel, 'filter' => ChannelMessagesFilter, 'pts' => int, 'limit' => int, ]);
```

Or, if you're into Lua:

```lua
updates.ChannelDifference = updates.getChannelDifference({force=Bool, channel=InputChannel, filter=ChannelMessagesFilter, pts=int, limit=int, })
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
|-500|No workers running|Internal error|
|-504|memory limit exit|Internal error|
|-503|Timeout|Timeout while fetching data|


