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
|photo\_small|[FileLocation](../types/FileLocation.md) | Yes|Location of the file corresponding to the small thumbnail for group profile photo|
|photo\_big|[FileLocation](../types/FileLocation.md) | Yes|Location of the file corresponding to the small thumbnail for group profile photo|
|dc\_id|[int](../types/int.md) | Yes|DC where this photo is stored|



### Type: [ChatPhoto](../types/ChatPhoto.md)


### Example:

```php
$chatPhoto = ['_' => 'chatPhoto', 'photo_small' => FileLocation, 'photo_big' => FileLocation, 'dc_id' => int];
```  


Or, if you're into Lua:

```lua
chatPhoto={_='chatPhoto', photo_small=FileLocation, photo_big=FileLocation, dc_id=int}

```


