---
title: channels.getBroadcastsForDiscussion
description: Get channels for discussion
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: channels.getBroadcastsForDiscussion  
[Back to methods index](index.md)


Get channels for discussion



### Return type: [messages\_Chats](../types/messages_Chats.md)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$messages_Chats = $MadelineProto->channels->getBroadcastsForDiscussion();
```

Or, if you're into Lua:

```lua
messages_Chats = channels.getBroadcastsForDiscussion({})
```

