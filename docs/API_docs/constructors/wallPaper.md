---
title: "wallPaper"
description: "Wallpaper settings."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: wallPaper  
[Back to constructors index](/API_docs/constructors/index.html)



Wallpaper settings.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[long](/API_docs/types/long.html) | Yes|Identifier|
|creator|[Bool](/API_docs/types/Bool.html) | Optional|Creator of the wallpaper|
|default|[Bool](/API_docs/types/Bool.html) | Optional|Whether this is the default wallpaper|
|pattern|[Bool](/API_docs/types/Bool.html) | Optional|Pattern|
|dark|[Bool](/API_docs/types/Bool.html) | Optional|Dark mode|
|access\_hash|[long](/API_docs/types/long.html) | Yes|Access hash|
|slug|[string](/API_docs/types/string.html) | Yes|Unique wallpaper ID|
|document|[Document](/API_docs/types/Document.html) | Optional|The actual wallpaper|
|settings|[WallPaperSettings](/API_docs/types/WallPaperSettings.html) | Optional|Wallpaper settings|



### Type: [WallPaper](/API_docs/types/WallPaper.html)


### Example:

```
$wallPaper = ['_' => 'wallPaper', 'id' => long, 'creator' => Bool, 'default' => Bool, 'pattern' => Bool, 'dark' => Bool, 'access_hash' => long, 'slug' => 'string', 'document' => Document, 'settings' => WallPaperSettings];
```  
