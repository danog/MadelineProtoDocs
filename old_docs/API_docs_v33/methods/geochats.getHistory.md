---
title: geochats.getHistory
description: Get geochat history
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/geochats_getHistory.html
---
# Method: geochats.getHistory  
[Back to methods index](index.md)


Get geochat history

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|peer|[InputGeoChat](../types/InputGeoChat.md) | The geochat | Yes|
|offset|[int](../types/int.md) | Offset | Yes|
|max\_id|[int](../types/int.md) | Maximum message ID | Yes|
|limit|[int](../types/int.md) | Number of results to return | Yes|


### Return type: [geochats.Messages](../types/geochats.Messages.md)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$geochats.Messages = $MadelineProto->geochats->getHistory(['peer' => InputGeoChat, 'offset' => int, 'max_id' => int, 'limit' => int, ]);
```

Or, if you're into Lua:

```lua
geochats.Messages = geochats.getHistory({peer=InputGeoChat, offset=int, max_id=int, limit=int, })
```

