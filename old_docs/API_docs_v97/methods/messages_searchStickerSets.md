---
title: messages.searchStickerSets
description: Find a sticker set
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Method: messages.searchStickerSets  
[Back to methods index](index.md)


Find a sticker set

### Parameters:

| Name     |    Type       | Description | Required |
|----------|---------------|-------------|----------|
|exclude\_featured|[Bool](../types/Bool.md) | Exclude featured sticker sets from the search? | Optional|
|q|[string](../types/string.md) | The search query | Yes|
|hash|Array of [int](../types/int.md) | The IDs of stickersets you already fetched | Optional|


### Return type: [messages\_FoundStickerSets](../types/messages_FoundStickerSets.md)

### Can bots use this method: **YES**


### MadelineProto Example:


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
define('MADELINE_BRANCH', '');
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

$messages_FoundStickerSets = $MadelineProto->messages->searchStickerSets(['exclude_featured' => Bool, 'q' => 'string', 'hash' => [int, int], ]);
```

Or, if you're into Lua:

```lua
messages_FoundStickerSets = messages.searchStickerSets({exclude_featured=Bool, q='string', hash={int}, })
```

