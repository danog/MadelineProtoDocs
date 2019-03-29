---
title: inputChatPhoto
description: Chat photo
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputChatPhoto  
[Back to constructors index](index.md)



Chat photo

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[MessageMedia, Message, Update or InputPhoto](../types/InputPhoto.md) | Optional|ID|
|crop|[InputPhotoCrop](../types/InputPhotoCrop.md) | Yes|Crop|



### Type: [InputChatPhoto](../types/InputChatPhoto.md)


### Example:

```php
$inputChatPhoto = ['_' => 'inputChatPhoto', 'id' => InputPhoto, 'crop' => InputPhotoCrop];
```  


Or, if you're into Lua:

```lua
inputChatPhoto={_='inputChatPhoto', id=InputPhoto, crop=InputPhotoCrop}

```


