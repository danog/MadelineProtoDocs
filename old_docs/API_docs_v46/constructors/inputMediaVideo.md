---
title: inputMediaVideo
description: Media video
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputMediaVideo  
[Back to constructors index](index.md)



Media video

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|video|[InputVideo](../types/InputVideo.md) | Optional|Video|
|caption|[string](../types/string.md) | Yes|Caption|



### Type: [InputMedia](../types/InputMedia.md)


### Example:

```php
$inputMediaVideo = ['_' => 'inputMediaVideo', 'video' => InputVideo, 'caption' => 'string'];
```  


Or, if you're into Lua:

```lua
inputMediaVideo={_='inputMediaVideo', video=InputVideo, caption='string'}

```


