---
title: "mediaAreaChannelPost"
description: "mediaAreaChannelPost attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: mediaAreaChannelPost  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|coordinates|[MediaAreaCoordinates](/API_docs/types/MediaAreaCoordinates.html) | Yes|
|channel\_id|[long](/API_docs/types/long.html) | Yes|
|msg\_id|[int](/API_docs/types/int.html) | Yes|



### Type: [MediaArea](/API_docs/types/MediaArea.html)


### Example:

```
$mediaAreaChannelPost = ['_' => 'mediaAreaChannelPost', 'coordinates' => MediaAreaCoordinates, 'channel_id' => long, 'msg_id' => int];
```  
