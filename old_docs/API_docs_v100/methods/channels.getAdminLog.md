---
title: channels.getAdminLog
description: Get the admin log of a [channel/supergroup](https://core.telegram.org/api/channel)
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: channels.getAdminLog  
[Back to methods index](index.md)


Get the admin log of a [channel/supergroup](https://core.telegram.org/api/channel)

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|channel|[Username, chat ID, Update, Message or InputChannel](../types/InputChannel.md) | Channel | Optional|
|q|[string](../types/string.md) | Search query, can be empty | Yes|
|events\_filter|[ChannelAdminLogEventsFilter](../types/ChannelAdminLogEventsFilter.md) | Event filter | Optional|
|admins|Array of [Username, chat ID, Update, Message or InputUser](../types/InputUser.md) | Fetch only actions from these admins | Optional|
|max\_id|[long](../types/long.md) | Maximum ID of message to return (see [pagination](https://core.telegram.org/api/offsets)) | Yes|
|min\_id|[long](../types/long.md) | Minimum ID of message to return (see [pagination](https://core.telegram.org/api/offsets)) | Yes|
|limit|[int](../types/int.md) | Maximum number of results to return, [see pagination](https://core.telegram.org/api/offsets) | Yes|


### Return type: [channels.AdminLogResults](../types/channels.AdminLogResults.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$channels.AdminLogResults = $MadelineProto->channels->getAdminLog(['channel' => InputChannel, 'q' => 'string', 'events_filter' => ChannelAdminLogEventsFilter, 'admins' => [InputUser, InputUser], 'max_id' => long, 'min_id' => long, 'limit' => int, ]);
```

Or, if you're into Lua:

```lua
channels.AdminLogResults = channels.getAdminLog({channel=InputChannel, q='string', events_filter=ChannelAdminLogEventsFilter, admins={InputUser}, max_id=long, min_id=long, limit=int, })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|CHANNEL_INVALID|The provided channel is invalid|
|400|CHANNEL_PRIVATE|You haven't joined this channel/supergroup|
|400|CHAT_ADMIN_REQUIRED|You must be an admin in this chat to do this|
|403|CHAT_WRITE_FORBIDDEN|You can't write in this chat|


