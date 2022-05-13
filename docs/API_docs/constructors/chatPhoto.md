---
title: "chatPhoto"
description: "Group profile photo."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: chatPhoto  
[Back to constructors index](/API_docs/constructors/index.html)



Group profile photo.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|has\_video|[Bool](/API_docs/types/Bool.html) | Optional|Whether the user has an animated profile picture|
|photo\_id|[long](/API_docs/types/long.html) | Yes|Photo ID|
|stripped\_thumb|[bytes](/API_docs/types/bytes.html) | Optional|[Stripped thumbnail](https://core.telegram.org/api/files#stripped-thumbnails)|
|dc\_id|[int](/API_docs/types/int.html) | Yes|DC where this photo is stored|



### Type: [ChatPhoto](/API_docs/types/ChatPhoto.html)


### Example:

```
$chatPhoto = ['_' => 'chatPhoto', 'has_video' => Bool, 'photo_id' => long, 'stripped_thumb' => 'bytes', 'dc_id' => int];
```  
