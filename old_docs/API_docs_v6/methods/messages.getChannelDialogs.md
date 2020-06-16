---
title: messages.getChannelDialogs
description: messages.getChannelDialogs parameters, return type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_getChannelDialogs.html
---
# Method: messages.getChannelDialogs
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

$messages.Dialogs = $MadelineProto->messages->getChannelDialogs(['offset' => int, 'limit' => int, ]);
```

Or, if you're into Lua:

```lua
messages.Dialogs = messages.getChannelDialogs({offset=int, limit=int, })
```

