---
title: "storyAlbum"
description: "Represents a story album »."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: storyAlbum  
[Back to constructors index](/API_docs/constructors/index.html)



Represents a [story album »](https://core.telegram.org/api/stories#story-albums).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|album\_id|[int](/API_docs/types/int.html) | Yes|ID of the album.|
|title|[string](/API_docs/types/string.html) | Yes|Name of the album.|
|icon\_photo|[Photo](/API_docs/types/Photo.html) | Optional|Photo from the first story of the album, if it's a photo.|
|icon\_video|[Document](/API_docs/types/Document.html) | Optional|Video from the first story of the album, if it's a video.|



### Type: [StoryAlbum](/API_docs/types/StoryAlbum.html)


### Example:

```
$storyAlbum = ['_' => 'storyAlbum', 'album_id' => int, 'title' => 'string', 'icon_photo' => Photo, 'icon_video' => Document];
```  
