---
title: messages.stickerSetInstallResultArchive
description: The stickerset was installed, but since there are too many stickersets some were archived
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messages.stickerSetInstallResultArchive  
[Back to constructors index](index.md)



The stickerset was installed, but since there are too many stickersets some were archived

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|sets|Array of [StickerSetCovered](../types/StickerSetCovered.md) | Yes|Sets|



### Type: [messages.StickerSetInstallResult](../types/messages.StickerSetInstallResult.md)


### Example:

```php
$messages.stickerSetInstallResultArchive = ['_' => 'messages.stickerSetInstallResultArchive', 'sets' => [StickerSetCovered, StickerSetCovered]];
```  


Or, if you're into Lua:

```lua
messages.stickerSetInstallResultArchive={_='messages.stickerSetInstallResultArchive', sets={StickerSetCovered}}

```


