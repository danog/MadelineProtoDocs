---
title: "messages.stickerSetInstallResultArchive"
description: "The stickerset was installed, but since there are too many stickersets some were archived"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/messages_stickerSetInstallResultArchive.html
---
# Constructor: messages.stickerSetInstallResultArchive  
[Back to constructors index](/API_docs/constructors/index.html)



The stickerset was installed, but since there are too many stickersets some were archived

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|sets|Array of [StickerSetCovered](/API_docs/types/StickerSetCovered.html) | Yes|Archived stickersets|



### Type: [messages.StickerSetInstallResult](/API_docs/types/messages.StickerSetInstallResult.html)


### Example:

```
$messages_stickerSetInstallResultArchive = ['_' => 'messages.stickerSetInstallResultArchive', 'sets' => [StickerSetCovered, StickerSetCovered]];
```  
