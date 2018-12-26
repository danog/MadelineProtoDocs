---
title: inputMediaUploadedAudio
description: Media uploaded audio
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputMediaUploadedAudio  
[Back to constructors index](index.md)



Media uploaded audio

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|file|[File path or InputFile](../types/InputFile.md) | Yes|File|
|duration|[int](../types/int.md) | Yes|Duration|
|mime\_type|[string](../types/string.md) | Optional|Mime type|



### Type: [InputMedia](../types/InputMedia.md)


### Example:

```php
$inputMediaUploadedAudio = ['_' => 'inputMediaUploadedAudio', 'file' => InputFile, 'duration' => int, 'mime_type' => 'string'];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "inputMediaUploadedAudio", "file": InputFile, "duration": int, "mime_type": "string"}
```


Or, if you're into Lua:

```lua
inputMediaUploadedAudio={_='inputMediaUploadedAudio', file=InputFile, duration=int, mime_type='string'}

```


