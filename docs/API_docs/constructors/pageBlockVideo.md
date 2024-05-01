---
title: "pageBlockVideo"
description: "Video"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: pageBlockVideo  
[Back to constructors index](/API_docs/constructors/index.html)



Video

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|autoplay|[Bool](/API_docs/types/Bool.html) | Optional|Whether the video is set to autoplay|
|loop|[Bool](/API_docs/types/Bool.html) | Optional|Whether the video is set to loop|
|video\_id|[long](/API_docs/types/long.html) | Yes|Video ID|
|caption|[PageCaption](/API_docs/types/PageCaption.html) | Yes|Caption|



### Type: [PageBlock](/API_docs/types/PageBlock.html)


### Example:

```
$pageBlockVideo = ['_' => 'pageBlockVideo', 'autoplay' => Bool, 'loop' => Bool, 'video_id' => long, 'caption' => PageCaption];
```  
