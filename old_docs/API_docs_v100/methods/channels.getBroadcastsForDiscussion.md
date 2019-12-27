---
title: channels.getBroadcastsForDiscussion
description: Get channels for discussion
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/channels_getBroadcastsForDiscussion.html
---
# Method: channels.getBroadcastsForDiscussion  
[Back to methods index](index.md)


Get channels for discussion



### Return type: [messages.Chats](../types/messages.Chats.md)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$messages.Chats = $MadelineProto->channels->getBroadcastsForDiscussion();
```

Or, if you're into Lua:

```lua
messages.Chats = channels.getBroadcastsForDiscussion({})
```

