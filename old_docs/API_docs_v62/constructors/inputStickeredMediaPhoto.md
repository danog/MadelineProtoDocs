---
title: inputStickeredMediaPhoto
description: Stickered media photo
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputStickeredMediaPhoto  
[Back to constructors index](index.md)



Stickered media photo

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[MessageMedia, Message, Update or InputPhoto](../types/InputPhoto.md) | Optional|ID|



### Type: [InputStickeredMedia](../types/InputStickeredMedia.md)


### Example:

```php
$inputStickeredMediaPhoto = ['_' => 'inputStickeredMediaPhoto', 'id' => InputPhoto];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "inputStickeredMediaPhoto", "id": InputPhoto}
```


Or, if you're into Lua:

```lua
inputStickeredMediaPhoto={_='inputStickeredMediaPhoto', id=InputPhoto}

```


