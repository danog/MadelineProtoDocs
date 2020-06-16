---
title: messageMediaPhoto
description: Attached photo.
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageMediaPhoto  
[Back to constructors index](index.md)



Attached photo.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|photo|[Photo](../types/Photo.md) | Optional|Photo|
|caption|[string](../types/string.md) | Yes|



### Type: [MessageMedia](../types/MessageMedia.md)


### Example:

```php
$messageMediaPhoto = ['_' => 'messageMediaPhoto', 'photo' => Photo, 'caption' => 'string'];
```  


Or, if you're into Lua:

```lua
messageMediaPhoto={_='messageMediaPhoto', photo=Photo, caption='string'}

```


