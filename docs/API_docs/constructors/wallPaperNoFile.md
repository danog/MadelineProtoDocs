---
title: "wallPaperNoFile"
description: "Represents a wallpaper only based on colors/gradients."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: wallPaperNoFile  
[Back to constructors index](/API_docs/constructors/index.html)



Represents a [wallpaper](https://core.telegram.org/api/wallpapers) only based on colors/gradients.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[long](/API_docs/types/long.html) | Yes|Wallpaper ID|
|default|[Bool](/API_docs/types/Bool.html) | Optional|Whether this is the default wallpaper|
|dark|[Bool](/API_docs/types/Bool.html) | Optional|Whether this wallpaper should be used in dark mode.|
|settings|[WallPaperSettings](/API_docs/types/WallPaperSettings.html) | Optional|Info on how to generate the wallpaper.|



### Type: [WallPaper](/API_docs/types/WallPaper.html)


### Example:

```
$wallPaperNoFile = ['_' => 'wallPaperNoFile', 'id' => long, 'default' => Bool, 'dark' => Bool, 'settings' => WallPaperSettings];
```  
