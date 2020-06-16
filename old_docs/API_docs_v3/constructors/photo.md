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
|id|[long](../types/long.md) | Yes|ID|
|access\_hash|[long](../types/long.md) | Yes|Access hash|
|user\_id|[int](../types/int.md) | Yes|
|date|[int](../types/int.md) | Yes|Date of upload|
|caption|[string](../types/string.md) | Yes|
|geo|[GeoPoint](../types/GeoPoint.md) | Optional|
|sizes|Array of [PhotoSize](../types/PhotoSize.md) | Yes|Available sizes for download|



### Type: [Photo](../types/Photo.md)


### Example:

```php
$photo = ['_' => 'photo', 'id' => long, 'access_hash' => long, 'user_id' => int, 'date' => int, 'caption' => 'string', 'geo' => GeoPoint, 'sizes' => [PhotoSize, PhotoSize]];
```  


Or, if you're into Lua:

```lua
photo={_='photo', id=long, access_hash=long, user_id=int, date=int, caption='string', geo=GeoPoint, sizes={PhotoSize}}

```


