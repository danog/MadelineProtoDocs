---
title: "channels.setDiscussionGroup"
description: "Associate a group to a channel as [discussion group](https://core.telegram.org/api/discussion) for that channel"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/channels_setDiscussionGroup.html
---
# Method: channels.setDiscussionGroup
[Back to methods index](index.md)



Associate a group to a channel as [discussion group](https://core.telegram.org/api/discussion) for that channel

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|broadcast|[Username, chat ID, Update, Message or InputChannel](../types/InputChannel.md) | Channel | Optional|
|group|[Username, chat ID, Update, Message or InputChannel](../types/InputChannel.md) | [Discussion group](https://core.telegram.org/api/discussion) to associate to the channel | Optional|


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

$Bool = $MadelineProto->channels->setDiscussionGroup(['broadcast' => InputChannel, 'group' => InputChannel, ]);
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|BROADCAST_ID_INVALID|Broadcast ID invalid|
|400|CHANNEL_INVALID|The provided channel is invalid|
|400|CHAT_ADMIN_REQUIRED|You must be an admin in this chat to do this|
|400|LINK_NOT_MODIFIED|Discussion link not modified|
|400|MEGAGROUP_ID_INVALID|Invalid supergroup ID|
|400|MEGAGROUP_PREHISTORY_HIDDEN|Group with hidden history for new members can't be set as discussion groups|


