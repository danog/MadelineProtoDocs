---
title: inputMediaUploadedThumbVideo
description: Media uploaded thumb video
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputMediaUploadedThumbVideo  
[Back to constructors index](index.md)



Media uploaded thumb video

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|file|[File path or InputFile](../types/InputFile.md) | Yes|File|
|thumb|[File path or InputFile](../types/InputFile.md) | Yes|Thumbnail|
|duration|[int](../types/int.md) | Yes|Duration|
|w|[int](../types/int.md) | Yes|Width|
|h|[int](../types/int.md) | Yes|Height|
|caption|[string](../types/string.md) | Yes|Caption|



### Type: [InputMedia](../types/InputMedia.md)


### Example:

```php
$inputMediaUploadedThumbVideo = ['_' => 'inputMediaUploadedThumbVideo', 'file' => InputFile, 'thumb' => InputFile, 'duration' => int, 'w' => int, 'h' => int, 'caption' => 'string'];
```  


Or, if you're into Lua:

```lua
inputMediaUploadedThumbVideo={_='inputMediaUploadedThumbVideo', file=InputFile, thumb=InputFile, duration=int, w=int, h=int, caption='string'}

```


