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
|id|[InputVideo](../types/InputVideo.md) | Optional|ID|
|caption|[string](../types/string.md) | Yes|Caption|



### Type: [InputMedia](../types/InputMedia.md)


### Example:

```php
$inputMediaVideo = ['_' => 'inputMediaVideo', 'id' => InputVideo, 'caption' => 'string'];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "inputMediaVideo", "id": InputVideo, "caption": "string"}
```


Or, if you're into Lua:

```lua
inputMediaVideo={_='inputMediaVideo', id=InputVideo, caption='string'}

```


