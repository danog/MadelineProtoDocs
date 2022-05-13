---
title: "wallPaperNoFile"
description: "Wallpaper with no file access hash, used for example when deleting (unsave=true) wallpapers using account.saveWallPaper, specifying just the wallpaper ID.  "
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: wallPaperNoFile  
[Back to constructors index](/API_docs/constructors/index.html)



Wallpaper with no file access hash, used for example when deleting (`unsave=true`) wallpapers using [account.saveWallPaper](../methods/account.saveWallPaper.html), specifying just the wallpaper ID.  
Also used for some default wallpapers which contain only colours.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[long](/API_docs/types/long.html) | Yes|Wallpaper ID|
|default|[Bool](/API_docs/types/Bool.html) | Optional|Whether this is the default wallpaper|
|dark|[Bool](/API_docs/types/Bool.html) | Optional|Dark mode|
|settings|[WallPaperSettings](/API_docs/types/WallPaperSettings.html) | Optional|Wallpaper settings|



### Type: [WallPaper](/API_docs/types/WallPaper.html)


### Example:

```
$wallPaperNoFile = ['_' => 'wallPaperNoFile', 'id' => long, 'default' => Bool, 'dark' => Bool, 'settings' => WallPaperSettings];
```  
