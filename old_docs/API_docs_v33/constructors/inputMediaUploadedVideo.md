---
title: inputMediaUploadedVideo
description: Media uploaded video
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputMediaUploadedVideo  
[Back to constructors index](index.md)



Media uploaded video

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|file|[File path or InputFile](../types/InputFile.md) | Yes|File|
|duration|[int](../types/int.md) | Yes|Duration|
|w|[int](../types/int.md) | Yes|Width|
|h|[int](../types/int.md) | Yes|Height|
|caption|[string](../types/string.md) | Yes|Caption|



### Type: [InputMedia](../types/InputMedia.md)


### Example:

```php
$inputMediaUploadedVideo = ['_' => 'inputMediaUploadedVideo', 'file' => InputFile, 'duration' => int, 'w' => int, 'h' => int, 'caption' => 'string'];
```  


Or, if you're into Lua:

```lua
inputMediaUploadedVideo={_='inputMediaUploadedVideo', file=InputFile, duration=int, w=int, h=int, caption='string'}

```


