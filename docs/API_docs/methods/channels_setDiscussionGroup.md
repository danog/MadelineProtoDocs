---
title: channels.setDiscussionGroup
description: Set discussion group of channel
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: channels.setDiscussionGroup  
[Back to methods index](index.md)


Set discussion group of channel

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|broadcast|[Username, chat ID, Update, Message or InputChannel](../types/InputChannel.md) | The channel | Optional|
|group|[Username, chat ID, Update, Message or InputChannel](../types/InputChannel.md) | The group | Optional|


### Return type: [Bool](../types/Bool.md)

### Can bots use this method: **YES**


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

