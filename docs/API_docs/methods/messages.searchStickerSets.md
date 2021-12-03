---
title: messages.searchStickerSets
description: Search for stickersets
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/messages_searchStickerSets.html
---
# Method: messages.searchStickerSets
[Back to methods index](index.md)



Search for stickersets

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|exclude\_featured|[Bool](../types/Bool.md) | Exclude featured stickersets from results | Optional|
|q|[string](../types/string.md) | Query string | Yes|
|hash|[long](../types/long.md) |  | Yes|


### Return type: [messages.FoundStickerSets](../types/messages.FoundStickerSets.md)

### Can bots use this method: **NO**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$messages_FoundStickerSets = $MadelineProto->messages->searchStickerSets(['exclude_featured' => Bool, 'q' => 'string', 'hash' => long, ]);
```

Or, if you're into Lua:

```lua
messages_FoundStickerSets = messages.searchStickerSets({exclude_featured=Bool, q='string', hash=long, })
```

