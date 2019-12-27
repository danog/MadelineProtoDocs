---
title: channels.getGroupsForDiscussion
description: Get all groups that can be used as [discussion groups](https://telegram.org/blog/privacy-discussions-web-bots)
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: channels.getGroupsForDiscussion  
[Back to methods index](index.md)


Get all groups that can be used as [discussion groups](https://telegram.org/blog/privacy-discussions-web-bots)



### Return type: [messages.Chats](../types/messages.Chats.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$messages.Chats = $MadelineProto->channels->getGroupsForDiscussion();
```

Or, if you're into Lua:

```lua
messages.Chats = channels.getGroupsForDiscussion({})
```

