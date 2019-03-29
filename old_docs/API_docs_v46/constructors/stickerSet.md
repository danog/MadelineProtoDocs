---
title: stickerSet
description: Sticker set
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: stickerSet  
[Back to constructors index](index.md)



Sticker set

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|installed|[Bool](../types/Bool.md) | Optional|Installed?|
|disabled|[Bool](../types/Bool.md) | Optional|Disabled?|
|official|[Bool](../types/Bool.md) | Optional|Official?|
|id|[long](../types/long.md) | Yes|ID|
|access\_hash|[long](../types/long.md) | Yes|Access hash|
|title|[string](../types/string.md) | Yes|Title|
|short\_name|[string](../types/string.md) | Yes|Short name|
|count|[int](../types/int.md) | Yes|Count|
|hash|[int](../types/int.md) | Yes|Hash|



### Type: [StickerSet](../types/StickerSet.md)


### Example:

```php
$stickerSet = ['_' => 'stickerSet', 'installed' => Bool, 'disabled' => Bool, 'official' => Bool, 'id' => long, 'access_hash' => long, 'title' => 'string', 'short_name' => 'string', 'count' => int, 'hash' => int];
```  


Or, if you're into Lua:

```lua
stickerSet={_='stickerSet', installed=Bool, disabled=Bool, official=Bool, id=long, access_hash=long, title='string', short_name='string', count=int, hash=int}

```


