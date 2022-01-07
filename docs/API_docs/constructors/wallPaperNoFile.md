---
title: "wallPaperNoFile"
description: "No file wallpaper"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: wallPaperNoFile  
[Back to constructors index](/API_docs/constructors/index.html)



No file wallpaper

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[long](/API_docs/types/long.html) | Yes|
|default|[Bool](/API_docs/types/Bool.html) | Optional|Whether this is the default wallpaper|
|dark|[Bool](/API_docs/types/Bool.html) | Optional|Dark mode|
|settings|[WallPaperSettings](/API_docs/types/WallPaperSettings.html) | Optional|Wallpaper settings|



### Type: [WallPaper](/API_docs/types/WallPaper.html)


### Example:

```php
$wallPaperNoFile = ['_' => 'wallPaperNoFile', 'id' => long, 'default' => Bool, 'dark' => Bool, 'settings' => WallPaperSettings];
```  
