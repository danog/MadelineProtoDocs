---
title: pageBlockVideo
description: Page block video
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: pageBlockVideo  
[Back to constructors index](index.md)



Page block video

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|autoplay|[Bool](../types/Bool.md) | Optional|Autoplay?|
|loop|[Bool](../types/Bool.md) | Optional|Loop?|
|video\_id|[long](../types/long.md) | Yes|Video ID|
|caption|[RichText](../types/RichText.md) | Yes|Caption|



### Type: [PageBlock](../types/PageBlock.md)


### Example:

```php
$pageBlockVideo = ['_' => 'pageBlockVideo', 'autoplay' => Bool, 'loop' => Bool, 'video_id' => long, 'caption' => RichText];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "pageBlockVideo", "autoplay": Bool, "loop": Bool, "video_id": long, "caption": RichText}
```


Or, if you're into Lua:

```lua
pageBlockVideo={_='pageBlockVideo', autoplay=Bool, loop=Bool, video_id=long, caption=RichText}

```


