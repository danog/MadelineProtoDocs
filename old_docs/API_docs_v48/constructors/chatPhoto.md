---
title: chatPhoto
description: Group profile photo.
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: chatPhoto  
[Back to constructors index](index.md)



Group profile photo.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|has\_video|[Bool](../types/Bool.md) | Optional|Whether the user has an animated profile picture|
|photo\_id|[long](../types/long.md) | Yes|
|stripped\_thumb|[bytes](../types/bytes.md) | Optional|
|dc\_id|[int](../types/int.md) | Yes|DC where this photo is stored|



### Type: [ChatPhoto](../types/ChatPhoto.md)


### Example:

```php
$chatPhoto = ['_' => 'chatPhoto', 'has_video' => Bool, 'photo_id' => long, 'stripped_thumb' => 'bytes', 'dc_id' => int];
```  


Or, if you're into Lua:

```lua
chatPhoto={_='chatPhoto', has_video=Bool, photo_id=long, stripped_thumb='bytes', dc_id=int}

```


