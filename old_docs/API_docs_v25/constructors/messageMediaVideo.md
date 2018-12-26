---
title: messageMediaVideo
description: Message media video
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageMediaVideo  
[Back to constructors index](index.md)



Message media video

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|video|[Video](../types/Video.md) | Optional|Video|



### Type: [MessageMedia](../types/MessageMedia.md)


### Example:

```php
$messageMediaVideo = ['_' => 'messageMediaVideo', 'video' => Video];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "messageMediaVideo", "video": Video}
```


Or, if you're into Lua:

```lua
messageMediaVideo={_='messageMediaVideo', video=Video}

```


