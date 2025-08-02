---
title: "stories.albums"
description: "stories.albums attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/stories_albums.html
---
# Constructor: stories.albums  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|hash|[long](/API_docs/types/long.html) | Yes|
|albums|Array of [StoryAlbum](/API_docs/types/StoryAlbum.html) | Yes|



### Type: [stories.Albums](/API_docs/types/stories.Albums.html)


### Example:

```
$stories_albums = ['_' => 'stories.albums', 'hash' => long, 'albums' => [StoryAlbum, StoryAlbum]];
```  
