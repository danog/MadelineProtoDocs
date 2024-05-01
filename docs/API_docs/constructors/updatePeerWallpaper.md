---
title: "updatePeerWallpaper"
description: "The wallpaper » of a given peer has changed."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updatePeerWallpaper  
[Back to constructors index](/API_docs/constructors/index.html)



The [wallpaper »](https://core.telegram.org/api/wallpapers) of a given peer has changed.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|wallpaper\_overridden|[Bool](/API_docs/types/Bool.html) | Optional|Whether the other user has chosen a custom wallpaper for us using [messages.setChatWallPaper](../methods/messages.setChatWallPaper.html) and the `for_both` flag, see [here »](https://core.telegram.org/api/wallpapers#installing-wallpapers-in-a-specific-chat-or-channel) for more info.|
|peer|[long](/API_docs/types/long.html) | Yes|The peer where the wallpaper has changed.|
|wallpaper|[WallPaper](/API_docs/types/WallPaper.html) | Optional|The new wallpaper, if none the wallpaper was removed and the default wallpaper should be used.|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updatePeerWallpaper = ['_' => 'updatePeerWallpaper', 'wallpaper_overridden' => Bool, 'peer' => long, 'wallpaper' => WallPaper];
```  
