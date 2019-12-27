---
title: messages.getChannelDialogs
description: Get channel/supergruop dialogs
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: messages.getChannelDialogs  
[Back to methods index](index.md)


Get channel/supergruop dialogs

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|offset|[int](../types/int.md) | Offset | Yes|
|limit|[int](../types/int.md) | Number of results to return | Yes|


### Return type: [messages.Dialogs](../types/messages.Dialogs.md)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$messages.Dialogs = $MadelineProto->messages->getChannelDialogs(['offset' => int, 'limit' => int, ]);
```

Or, if you're into Lua:

```lua
messages.Dialogs = messages.getChannelDialogs({offset=int, limit=int, })
```

