---
title: "channels.getAdminLog"
description: "Get the admin log of a [channel/supergroup](https://core.telegram.org/api/channel)"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/channels_getAdminLog.html
---
# Method: channels.getAdminLog
[Back to methods index](index.html)



Get the admin log of a [channel/supergroup](https://core.telegram.org/api/channel)

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|channel|[Username, chat ID, Update, Message or InputChannel](/API_docs/types/InputChannel.html) | Channel | Optional|
|q|[string](/API_docs/types/string.html) | Search query, can be empty | Yes|
|events\_filter|[ChannelAdminLogEventsFilter](/API_docs/types/ChannelAdminLogEventsFilter.html) | Event filter | Optional|
|admins|Array of [Username, chat ID, Update, Message or InputUser](/API_docs/types/InputUser.html) | Only show events from these admins | Optional|
|max\_id|[long](/API_docs/types/long.html) | Maximum ID of message to return (see [pagination](https://core.telegram.org/api/offsets)) | Yes|
|min\_id|[long](/API_docs/types/long.html) | Minimum ID of message to return (see [pagination](https://core.telegram.org/api/offsets)) | Yes|
|limit|[int](/API_docs/types/int.html) | Maximum number of results to return, [see pagination](https://core.telegram.org/api/offsets) | Yes|


### Return type: [channels.AdminLogResults](/API_docs/types/channels.AdminLogResults.html)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

// PHP 8+ syntax, use an array on PHP 7.
$channels_AdminLogResults = $MadelineProto->channels->getAdminLog(channel: InputChannel, q: 'string', events_filter: ChannelAdminLogEventsFilter, admins: [InputUser, InputUser], max_id: long, min_id: long, limit: int, );
```

