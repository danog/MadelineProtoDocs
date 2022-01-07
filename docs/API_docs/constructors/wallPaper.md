---
title: "wallPaper"
description: "Wallpaper settings."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: wallPaper  
[Back to constructors index](/API_docs/constructors/index.md)



Wallpaper settings.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[long](/API_docs/types/long.md) | Yes|Identifier|
|creator|[Bool](/API_docs/types/Bool.md) | Optional|Creator of the wallpaper|
|default|[Bool](/API_docs/types/Bool.md) | Optional|Whether this is the default wallpaper|
|pattern|[Bool](/API_docs/types/Bool.md) | Optional|Pattern|
|dark|[Bool](/API_docs/types/Bool.md) | Optional|Dark mode|
|access\_hash|[long](/API_docs/types/long.md) | Yes|Access hash|
|slug|[string](/API_docs/types/string.md) | Yes|Unique wallpaper ID|
|document|[Document](/API_docs/types/Document.md) | Optional|The actual wallpaper|
|settings|[WallPaperSettings](/API_docs/types/WallPaperSettings.md) | Optional|Wallpaper settings|



### Type: [WallPaper](/API_docs/types/WallPaper.md)


### Example:

```php
$wallPaper = ['_' => 'wallPaper', 'id' => long, 'creator' => Bool, 'default' => Bool, 'pattern' => Bool, 'dark' => Bool, 'access_hash' => long, 'slug' => 'string', 'document' => Document, 'settings' => WallPaperSettings];
```  
