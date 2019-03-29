---
title: audio
description: Audio
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: audio  
[Back to constructors index](index.md)



Audio

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[long](../types/long.md) | Yes|ID|
|access\_hash|[long](../types/long.md) | Yes|Access hash|
|user\_id|[int](../types/int.md) | Yes|User ID|
|date|[int](../types/int.md) | Yes|Date|
|duration|[int](../types/int.md) | Yes|Duration|
|mime\_type|[string](../types/string.md) | Yes|Mime type|
|size|[int](../types/int.md) | Yes|Size|
|dc\_id|[int](../types/int.md) | Yes|DC ID|



### Type: [Audio](../types/Audio.md)


### Example:

```php
$audio = ['_' => 'audio', 'id' => long, 'access_hash' => long, 'user_id' => int, 'date' => int, 'duration' => int, 'mime_type' => 'string', 'size' => int, 'dc_id' => int];
```  


Or, if you're into Lua:

```lua
audio={_='audio', id=long, access_hash=long, user_id=int, date=int, duration=int, mime_type='string', size=int, dc_id=int}

```


