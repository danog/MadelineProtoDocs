---
title: messageMediaVideo
description: messageMediaVideo attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageMediaVideo  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|video|[Video](../types/Video.md) | Optional|
|caption|[string](../types/string.md) | Yes|



### Type: [MessageMedia](../types/MessageMedia.md)


### Example:

```php
$messageMediaVideo = ['_' => 'messageMediaVideo', 'video' => Video, 'caption' => 'string'];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "messageMediaVideo", "video": Video, "caption": "string"}
```


Or, if you're into Lua:

```lua
messageMediaVideo={_='messageMediaVideo', video=Video, caption='string'}

```


