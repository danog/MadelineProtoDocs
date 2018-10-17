---
title: inputMediaUploadedPhoto
description: inputMediaUploadedPhoto attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputMediaUploadedPhoto  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|file|[File path or InputFile](../types/InputFile.md) | Yes|
|caption|[string](../types/string.md) | Yes|



### Type: [InputMedia](../types/InputMedia.md)


### Example:

```php
$inputMediaUploadedPhoto = ['_' => 'inputMediaUploadedPhoto', 'file' => InputFile, 'caption' => 'string'];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "inputMediaUploadedPhoto", "file": InputFile, "caption": "string"}
```


Or, if you're into Lua:

```lua
inputMediaUploadedPhoto={_='inputMediaUploadedPhoto', file=InputFile, caption='string'}

```


