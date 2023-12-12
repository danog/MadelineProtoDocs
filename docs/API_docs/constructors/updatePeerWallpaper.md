---
title: "updatePeerWallpaper"
description: "updatePeerWallpaper attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updatePeerWallpaper  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|wallpaper\_overridden|[Bool](/API_docs/types/Bool.html) | Optional|
|peer|[long](/API_docs/types/long.html) | Yes|
|wallpaper|[WallPaper](/API_docs/types/WallPaper.html) | Optional|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updatePeerWallpaper = ['_' => 'updatePeerWallpaper', 'wallpaper_overridden' => Bool, 'peer' => long, 'wallpaper' => WallPaper];
```  
