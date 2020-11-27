---
title: messages.getArchivedStickers
description: Get all archived stickers
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_getArchivedStickers.html
---
# Method: messages.getArchivedStickers
[Back to methods index](index.md)



Get all archived stickers

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|offset\_id|[long](../types/long.md) | [Offsets for pagination, for more info click here](https://core.telegram.org/api/offsets) | Yes|
|limit|[int](../types/int.md) | Maximum number of results to return, [see pagination](https://core.telegram.org/api/offsets) | Yes|


### Return type: [messages.ArchivedStickers](../types/messages.ArchivedStickers.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$messages_ArchivedStickers = $MadelineProto->messages->getArchivedStickers(['offset_id' => long, 'limit' => int, ]);
```

Or, if you're into Lua:

```lua
messages_ArchivedStickers = messages.getArchivedStickers({offset_id=long, limit=int, })
```

