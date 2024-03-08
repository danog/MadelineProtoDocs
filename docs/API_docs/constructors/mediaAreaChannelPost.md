---
title: "mediaAreaChannelPost"
description: "Represents a channel post."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: mediaAreaChannelPost  
[Back to constructors index](/API_docs/constructors/index.html)



Represents a channel post.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|coordinates|[MediaAreaCoordinates](/API_docs/types/MediaAreaCoordinates.html) | Yes|The size and location of the media area corresponding to the location sticker on top of the story media.|
|channel\_id|[long](/API_docs/types/long.html) | Yes|The channel that posted the message|
|msg\_id|[int](/API_docs/types/int.html) | Yes|ID of the channel message|



### Type: [MediaArea](/API_docs/types/MediaArea.html)


### Example:

```
$mediaAreaChannelPost = ['_' => 'mediaAreaChannelPost', 'coordinates' => MediaAreaCoordinates, 'channel_id' => long, 'msg_id' => int];
```  
