---
title: messages.stickerSetInstallResultArchive
description: Sticker set install result archive
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messages.stickerSetInstallResultArchive  
[Back to constructors index](index.md)



Sticker set install result archive

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|sets|Array of [StickerSetCovered](../types/StickerSetCovered.md) | Yes|Sets|



### Type: [messages\_StickerSetInstallResult](../types/messages_StickerSetInstallResult.md)


### Example:

```php
$messages_stickerSetInstallResultArchive = ['_' => 'messages.stickerSetInstallResultArchive', 'sets' => [StickerSetCovered, StickerSetCovered]];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "messages.stickerSetInstallResultArchive", "sets": [StickerSetCovered]}
```


Or, if you're into Lua:

```lua
messages_stickerSetInstallResultArchive={_='messages.stickerSetInstallResultArchive', sets={StickerSetCovered}}

```


