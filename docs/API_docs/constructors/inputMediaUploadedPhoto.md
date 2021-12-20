---
title: "inputMediaUploadedPhoto"
description: "Photo"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputMediaUploadedPhoto  
[Back to constructors index](index.md)



Photo

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|file|[File path or InputFile](../types/InputFile.md) | Yes|The [uploaded file](https://core.telegram.org/api/files)|
|stickers|Array of [MessageMedia, Message, Update or InputDocument](../types/InputDocument.md) | Optional|Attached mask stickers|
|ttl\_seconds|[int](../types/int.md) | Optional|Time to live in seconds of self-destructing photo|



### Type: [InputMedia](../types/InputMedia.md)


### Example:

```php
$inputMediaUploadedPhoto = ['_' => 'inputMediaUploadedPhoto', 'file' => InputFile, 'stickers' => [InputDocument, InputDocument], 'ttl_seconds' => int];
```  


Or, if you're into Lua:

```lua
inputMediaUploadedPhoto={_='inputMediaUploadedPhoto', file=InputFile, stickers={InputDocument}, ttl_seconds=int}

```


