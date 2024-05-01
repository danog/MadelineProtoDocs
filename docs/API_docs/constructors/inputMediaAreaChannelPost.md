---
title: "inputMediaAreaChannelPost"
description: "Represents a channel post"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputMediaAreaChannelPost  
[Back to constructors index](/API_docs/constructors/index.html)



Represents a channel post

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|coordinates|[MediaAreaCoordinates](/API_docs/types/MediaAreaCoordinates.html) | Yes|The size and location of the media area corresponding to the location sticker on top of the story media.|
|channel|[InputChannel](/API_docs/types/InputChannel.html) | Optional|The channel that posted the message|
|msg\_id|[int](/API_docs/types/int.html) | Yes|ID of the channel message|



### Type: [MediaArea](/API_docs/types/MediaArea.html)


### Example:

```
$inputMediaAreaChannelPost = ['_' => 'inputMediaAreaChannelPost', 'coordinates' => MediaAreaCoordinates, 'channel' => InputChannel, 'msg_id' => int];
```  
