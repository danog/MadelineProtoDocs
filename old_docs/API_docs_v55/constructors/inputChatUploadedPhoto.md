---
title: inputChatUploadedPhoto
description: Chat uploaded photo
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputChatUploadedPhoto  
[Back to constructors index](index.md)



Chat uploaded photo

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|file|[File path or InputFile](../types/InputFile.md) | Yes|File|
|crop|[InputPhotoCrop](../types/InputPhotoCrop.md) | Yes|Crop|



### Type: [InputChatPhoto](../types/InputChatPhoto.md)


### Example:

```php
$inputChatUploadedPhoto = ['_' => 'inputChatUploadedPhoto', 'file' => InputFile, 'crop' => InputPhotoCrop];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "inputChatUploadedPhoto", "file": InputFile, "crop": InputPhotoCrop}
```


Or, if you're into Lua:

```lua
inputChatUploadedPhoto={_='inputChatUploadedPhoto', file=InputFile, crop=InputPhotoCrop}

```


