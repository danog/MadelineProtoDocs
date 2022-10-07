---
title: "wallPaper"
description: "Represents a wallpaper based on an image."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: wallPaper  
[Back to constructors index](/API_docs/constructors/index.html)



Represents a [wallpaper](https://core.telegram.org/api/wallpapers) based on an image.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[long](/API_docs/types/long.html) | Yes|Identifier|
|creator|[Bool](/API_docs/types/Bool.html) | Optional|Whether we created this wallpaper|
|default|[Bool](/API_docs/types/Bool.html) | Optional|Whether this is the default wallpaper|
|pattern|[Bool](/API_docs/types/Bool.html) | Optional|Whether this is a [pattern wallpaper »](https://core.telegram.org/api/wallpapers#pattern-wallpapers)|
|dark|[Bool](/API_docs/types/Bool.html) | Optional|Whether this wallpaper should be used in dark mode.|
|access\_hash|[long](/API_docs/types/long.html) | Yes|Access hash|
|slug|[string](/API_docs/types/string.html) | Yes|Unique wallpaper ID, used when generating [wallpaper links](https://core.telegram.org/api/links#wallpaper-links) or [importing wallpaper links](https://core.telegram.org/api/wallpapers).|
|document|[Document](/API_docs/types/Document.html) | Optional|The actual wallpaper|
|settings|[WallPaperSettings](/API_docs/types/WallPaperSettings.html) | Optional|Info on how to generate the wallpaper, according to [these instructions »](https://core.telegram.org/api/wallpapers).|



### Type: [WallPaper](/API_docs/types/WallPaper.html)


### Example:

```
$wallPaper = ['_' => 'wallPaper', 'id' => long, 'creator' => Bool, 'default' => Bool, 'pattern' => Bool, 'dark' => Bool, 'access_hash' => long, 'slug' => 'string', 'document' => Document, 'settings' => WallPaperSettings];
```  
