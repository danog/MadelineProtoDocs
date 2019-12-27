---
title: messages.archivedStickers
description: Archived stickersets
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messages.archivedStickers  
[Back to constructors index](index.md)



Archived stickersets

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|count|[int](../types/int.md) | Yes|Number of archived stickers|
|sets|Array of [StickerSetCovered](../types/StickerSetCovered.md) | Yes|Sets|



### Type: [messages\_ArchivedStickers](../types/messages_ArchivedStickers.md)


### Example:

```php
$messages_archivedStickers = ['_' => 'messages.archivedStickers', 'count' => int, 'sets' => [StickerSetCovered, StickerSetCovered]];
```  


Or, if you're into Lua:

```lua
messages_archivedStickers={_='messages.archivedStickers', count=int, sets={StickerSetCovered}}

```

