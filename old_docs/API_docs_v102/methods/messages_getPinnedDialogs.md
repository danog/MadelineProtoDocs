---
title: messages.getPinnedDialogs
description: Get pinned dialogs
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: messages.getPinnedDialogs  
[Back to methods index](index.md)


Get pinned dialogs

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|folder\_id|[int](../types/int.md) | Folder ID | Yes|


### Return type: [messages\_PeerDialogs](../types/messages_PeerDialogs.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$messages_PeerDialogs = $MadelineProto->messages->getPinnedDialogs(['folder_id' => int, ]);
```

Or, if you're into Lua:

```lua
messages_PeerDialogs = messages.getPinnedDialogs({folder_id=int, })
```

