---
title: channels.getDialogs
description: channels.getDialogs parameters, return type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/channels_getDialogs.html
---
# Method: channels.getDialogs
[Back to methods index](index.md)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|offset|[int](../types/int.md) | Yes|
|limit|[int](../types/int.md) | Yes|


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

$messages.Dialogs = $MadelineProto->channels->getDialogs(['offset' => int, 'limit' => int, ]);
```

Or, if you're into Lua:

```lua
messages.Dialogs = channels.getDialogs({offset=int, limit=int, })
```

