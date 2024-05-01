---
title: "messageActionSetChatWallPaper"
description: "The wallpaper » of the current chat was changed."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageActionSetChatWallPaper  
[Back to constructors index](/API_docs/constructors/index.html)



The [wallpaper »](https://core.telegram.org/api/wallpapers) of the current chat was changed.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|same|[Bool](/API_docs/types/Bool.html) | Optional|If set, indicates the user applied a [wallpaper »](https://core.telegram.org/api/wallpapers) previously sent by the other user in a [messageActionSetChatWallPaper](../constructors/messageActionSetChatWallPaper.html) message.|
|for\_both|[Bool](/API_docs/types/Bool.html) | Optional|If set, indicates the wallpaper was forcefully applied for both sides, without explicit confirmation from the other side. <br>If the message is incoming, and we did not like the new wallpaper the other user has chosen for us, we can re-set our previous wallpaper just on our side, by invoking [messages.setChatWallPaper](../methods/messages.setChatWallPaper.html), providing only the `revert` flag (and obviously the `peer` parameter).|
|wallpaper|[WallPaper](/API_docs/types/WallPaper.html) | Yes|New [wallpaper](https://core.telegram.org/api/wallpapers)|



### Type: [MessageAction](/API_docs/types/MessageAction.html)


### Example:

```
$messageActionSetChatWallPaper = ['_' => 'messageActionSetChatWallPaper', 'same' => Bool, 'for_both' => Bool, 'wallpaper' => WallPaper];
```  
