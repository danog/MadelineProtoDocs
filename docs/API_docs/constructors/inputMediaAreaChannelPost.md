---
title: "inputMediaAreaChannelPost"
description: "inputMediaAreaChannelPost attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputMediaAreaChannelPost  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|coordinates|[MediaAreaCoordinates](/API_docs/types/MediaAreaCoordinates.html) | Yes|
|channel|[InputChannel](/API_docs/types/InputChannel.html) | Optional|
|msg\_id|[int](/API_docs/types/int.html) | Yes|



### Type: [MediaArea](/API_docs/types/MediaArea.html)


### Example:

```
$inputMediaAreaChannelPost = ['_' => 'inputMediaAreaChannelPost', 'coordinates' => MediaAreaCoordinates, 'channel' => InputChannel, 'msg_id' => int];
```  
