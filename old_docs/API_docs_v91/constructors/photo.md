---
title: photo
description: Photo
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: photo  
[Back to constructors index](index.md)



Photo

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|has\_stickers|[Bool](../types/Bool.md) | Optional|Has stickers?|
|id|[long](../types/long.md) | Yes|ID|
|access\_hash|[long](../types/long.md) | Yes|Access hash|
|file\_reference|[bytes](../types/bytes.md) | Yes|File reference|
|date|[int](../types/int.md) | Yes|Date|
|sizes|Array of [PhotoSize](../types/PhotoSize.md) | Yes|Sizes|



### Type: [Photo](../types/Photo.md)


### Example:

```php
$photo = ['_' => 'photo', 'has_stickers' => Bool, 'id' => long, 'access_hash' => long, 'file_reference' => 'bytes', 'date' => int, 'sizes' => [PhotoSize, PhotoSize]];
```  


Or, if you're into Lua:

```lua
photo={_='photo', has_stickers=Bool, id=long, access_hash=long, file_reference='bytes', date=int, sizes={PhotoSize}}

```


