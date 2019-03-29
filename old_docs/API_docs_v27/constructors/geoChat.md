---
title: geoChat
description: Geo chat
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: geoChat  
[Back to constructors index](index.md)



Geo chat

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[int](../types/int.md) | Yes|ID|
|access\_hash|[long](../types/long.md) | Yes|Access hash|
|title|[string](../types/string.md) | Yes|Title|
|address|[string](../types/string.md) | Yes|Address|
|venue|[string](../types/string.md) | Yes|Venue|
|geo|[GeoPoint](../types/GeoPoint.md) | Optional|Geo|
|photo|[ChatPhoto](../types/ChatPhoto.md) | Optional|Photo|
|participants\_count|[int](../types/int.md) | Yes|Participants count|
|date|[int](../types/int.md) | Yes|Date|
|checked\_in|[Bool](../types/Bool.md) | Yes|Checked in?|
|version|[int](../types/int.md) | Yes|Version|



### Type: [Chat](../types/Chat.md)


### Example:

```php
$geoChat = ['_' => 'geoChat', 'id' => int, 'access_hash' => long, 'title' => 'string', 'address' => 'string', 'venue' => 'string', 'geo' => GeoPoint, 'photo' => ChatPhoto, 'participants_count' => int, 'date' => int, 'checked_in' => Bool, 'version' => int];
```  


Or, if you're into Lua:

```lua
geoChat={_='geoChat', id=int, access_hash=long, title='string', address='string', venue='string', geo=GeoPoint, photo=ChatPhoto, participants_count=int, date=int, checked_in=Bool, version=int}

```


