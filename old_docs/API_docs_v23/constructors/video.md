---
title: video
description: Video
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: video  
[Back to constructors index](index.md)



Video

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[long](../types/long.md) | Yes|ID|
|access\_hash|[long](../types/long.md) | Yes|Access hash|
|user\_id|[int](../types/int.md) | Yes|User ID|
|date|[int](../types/int.md) | Yes|Date|
|caption|[string](../types/string.md) | Yes|Caption|
|duration|[int](../types/int.md) | Yes|Duration|
|mime\_type|[string](../types/string.md) | Yes|Mime type|
|size|[int](../types/int.md) | Yes|Size|
|thumb|[PhotoSize](../types/PhotoSize.md) | Optional|Thumbnail|
|dc\_id|[int](../types/int.md) | Yes|DC ID|
|w|[int](../types/int.md) | Yes|Width|
|h|[int](../types/int.md) | Yes|Height|



### Type: [Video](../types/Video.md)


### Example:

```php
$video = ['_' => 'video', 'id' => long, 'access_hash' => long, 'user_id' => int, 'date' => int, 'caption' => 'string', 'duration' => int, 'mime_type' => 'string', 'size' => int, 'thumb' => PhotoSize, 'dc_id' => int, 'w' => int, 'h' => int];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "video", "id": long, "access_hash": long, "user_id": int, "date": int, "caption": "string", "duration": int, "mime_type": "string", "size": int, "thumb": PhotoSize, "dc_id": int, "w": int, "h": int}
```


Or, if you're into Lua:

```lua
video={_='video', id=long, access_hash=long, user_id=int, date=int, caption='string', duration=int, mime_type='string', size=int, thumb=PhotoSize, dc_id=int, w=int, h=int}

```


