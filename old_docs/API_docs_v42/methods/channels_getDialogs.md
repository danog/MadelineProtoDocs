---
title: channels.getDialogs
description: Get channel dialogs
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: channels.getDialogs  
[Back to methods index](index.md)


Get channel dialogs

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|offset|[int](../types/int.md) | Offset | Yes|
|limit|[int](../types/int.md) | Number of results to return | Yes|


### Return type: [messages\_Dialogs](../types/messages_Dialogs.md)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
define('MADELINE_BRANCH', '');
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$messages_Dialogs = $MadelineProto->channels->getDialogs(['offset' => int, 'limit' => int, ]);
```

Or, if you're into Lua:

```lua
messages_Dialogs = channels.getDialogs({offset=int, limit=int, })
```

