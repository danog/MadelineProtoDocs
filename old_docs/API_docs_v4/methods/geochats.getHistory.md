---
title: geochats.getHistory
description: geochats.getHistory parameters, return type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/geochats_getHistory.html
---
# Method: geochats.getHistory
[Back to methods index](index.md)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|peer|[InputGeoChat](../types/InputGeoChat.md) | Yes|
|offset|[int](../types/int.md) | Yes|
|max\_id|[int](../types/int.md) | Yes|
|limit|[int](../types/int.md) | Yes|


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

$geochats_Messages = $MadelineProto->geochats->getHistory(['peer' => InputGeoChat, 'offset' => int, 'max_id' => int, 'limit' => int, ]);
```

Or, if you're into Lua:

```lua
geochats_Messages = geochats.getHistory({peer=InputGeoChat, offset=int, max_id=int, limit=int, })
```

