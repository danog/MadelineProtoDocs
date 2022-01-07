---
title: "wallPaperNoFile"
description: "No file wallpaper"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: wallPaperNoFile  
[Back to constructors index](/API_docs/constructors/index.md)



No file wallpaper

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[long](/API_docs/types/long.md) | Yes|
|default|[Bool](/API_docs/types/Bool.md) | Optional|Whether this is the default wallpaper|
|dark|[Bool](/API_docs/types/Bool.md) | Optional|Dark mode|
|settings|[WallPaperSettings](/API_docs/types/WallPaperSettings.md) | Optional|Wallpaper settings|



### Type: [WallPaper](/API_docs/types/WallPaper.md)


### Example:

```php
$wallPaperNoFile = ['_' => 'wallPaperNoFile', 'id' => long, 'default' => Bool, 'dark' => Bool, 'settings' => WallPaperSettings];
```  
