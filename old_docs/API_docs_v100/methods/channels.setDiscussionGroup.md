---
title: channels.setDiscussionGroup
description: Associate a group to a channel as [discussion group](https://telegram.org/blog/privacy-discussions-web-bots) for that channel
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: channels.setDiscussionGroup  
[Back to methods index](index.md)


Associate a group to a channel as [discussion group](https://telegram.org/blog/privacy-discussions-web-bots) for that channel

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|broadcast|[Username, chat ID, Update, Message or InputChannel](../types/InputChannel.md) | Channel | Optional|
|group|[Username, chat ID, Update, Message or InputChannel](../types/InputChannel.md) | Discussion group to associate to the channel | Optional|


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

Or, if you're into Lua:

```lua
Bool = channels.setDiscussionGroup({broadcast=InputChannel, group=InputChannel, })
```

### Errors

| Code | Type     | Description   |
|------|----------|---------------|
|400|BROADCAST_ID_INVALID|Broadcast ID invalid|
|400|LINK_NOT_MODIFIED|Discussion link not modified|
|400|MEGAGROUP_ID_INVALID|Invalid supergroup ID|


