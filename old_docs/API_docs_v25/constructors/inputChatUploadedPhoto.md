---
title: inputChatUploadedPhoto
description: New photo to be set as group profile photo.
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputChatUploadedPhoto  
[Back to constructors index](index.md)



New photo to be set as group profile photo.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|file|[File path or InputFile](../types/InputFile.md) | Yes|File saved in parts using the method [upload.saveFilePart](../methods/upload.saveFilePart.md)|
|crop|[InputPhotoCrop](../types/InputPhotoCrop.md) | Yes|Crop|



### Type: [InputChatPhoto](../types/InputChatPhoto.md)


### Example:

```php
$inputChatUploadedPhoto = ['_' => 'inputChatUploadedPhoto', 'file' => InputFile, 'crop' => InputPhotoCrop];
```  


Or, if you're into Lua:

```lua
inputChatUploadedPhoto={_='inputChatUploadedPhoto', file=InputFile, crop=InputPhotoCrop}

```


