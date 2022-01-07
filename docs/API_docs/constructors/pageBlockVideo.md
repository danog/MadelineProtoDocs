---
title: "pageBlockVideo"
description: "Video"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: pageBlockVideo  
[Back to constructors index](index.md)



Video

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|autoplay|[Bool](../types/Bool.md) | Optional|Whether the video is set to autoplay|
|loop|[Bool](../types/Bool.md) | Optional|Whether the video is set to loop|
|video\_id|[long](../types/long.md) | Yes|Video ID|
|caption|[PageCaption](../types/PageCaption.md) | Yes|Caption|



### Type: [PageBlock](../types/PageBlock.md)


### Example:

```php
$pageBlockVideo = ['_' => 'pageBlockVideo', 'autoplay' => Bool, 'loop' => Bool, 'video_id' => long, 'caption' => PageCaption];
```  
