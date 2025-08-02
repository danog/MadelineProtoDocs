---
title: "storyAlbum"
description: "storyAlbum attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: storyAlbum  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|album\_id|[int](/API_docs/types/int.html) | Yes|
|title|[string](/API_docs/types/string.html) | Yes|
|icon\_photo|[Photo](/API_docs/types/Photo.html) | Optional|
|icon\_video|[Document](/API_docs/types/Document.html) | Optional|



### Type: [StoryAlbum](/API_docs/types/StoryAlbum.html)


### Example:

```
$storyAlbum = ['_' => 'storyAlbum', 'album_id' => int, 'title' => 'string', 'icon_photo' => Photo, 'icon_video' => Document];
```  
