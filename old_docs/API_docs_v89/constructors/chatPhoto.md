---
title: chatPhoto
description: Chat photo
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: chatPhoto  
[Back to constructors index](index.md)



Chat photo

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|photo\_small|[FileLocation](../types/FileLocation.md) | Yes|Photo small|
|photo\_big|[FileLocation](../types/FileLocation.md) | Yes|Photo big|



### Type: [ChatPhoto](../types/ChatPhoto.md)


### Example:

```php
$chatPhoto = ['_' => 'chatPhoto', 'photo_small' => FileLocation, 'photo_big' => FileLocation];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "chatPhoto", "photo_small": FileLocation, "photo_big": FileLocation}
```


Or, if you're into Lua:

```lua
chatPhoto={_='chatPhoto', photo_small=FileLocation, photo_big=FileLocation}

```


