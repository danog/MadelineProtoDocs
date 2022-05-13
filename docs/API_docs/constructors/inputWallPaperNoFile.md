---
title: "inputWallPaperNoFile"
description: "Wallpaper with no file access hash, used for example when deleting (unsave=true) wallpapers using account.saveWallPaper, specifying just the wallpaper ID."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputWallPaperNoFile  
[Back to constructors index](/API_docs/constructors/index.html)



Wallpaper with no file access hash, used for example when deleting (`unsave=true`) wallpapers using [account.saveWallPaper](../methods/account.saveWallPaper.html), specifying just the wallpaper ID.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[long](/API_docs/types/long.html) | Yes|Wallpaper ID|



### Type: [InputWallPaper](/API_docs/types/InputWallPaper.html)


### Example:

```
$inputWallPaperNoFile = ['_' => 'inputWallPaperNoFile', 'id' => long];
```  
