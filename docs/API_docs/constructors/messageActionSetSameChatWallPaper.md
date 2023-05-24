---
title: "messageActionSetSameChatWallPaper"
description: "The user applied a wallpaper » previously sent by the other user in a messageActionSetChatWallPaper message."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageActionSetSameChatWallPaper  
[Back to constructors index](/API_docs/constructors/index.html)



The user applied a [wallpaper »](https://core.telegram.org/api/wallpapers) previously sent by the other user in a [messageActionSetChatWallPaper](../constructors/messageActionSetChatWallPaper.html) message.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|wallpaper|[WallPaper](/API_docs/types/WallPaper.html) | Yes|The [wallpaper](https://core.telegram.org/api/wallpapers)|



### Type: [MessageAction](/API_docs/types/MessageAction.html)


### Example:

```
$messageActionSetSameChatWallPaper = ['_' => 'messageActionSetSameChatWallPaper', 'wallpaper' => WallPaper];
```  
