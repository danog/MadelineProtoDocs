---
title: messages.foundStickerSets
description: Found sticker sets
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messages.foundStickerSets  
[Back to constructors index](index.md)



Found sticker sets

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|hash|[int](../types/int.md) | Yes|Hash|
|sets|Array of [StickerSetCovered](../types/StickerSetCovered.md) | Yes|Sets|



### Type: [messages\_FoundStickerSets](../types/messages_FoundStickerSets.md)


### Example:

```php
$messages_foundStickerSets = ['_' => 'messages.foundStickerSets', 'hash' => int, 'sets' => [StickerSetCovered, StickerSetCovered]];
```  


Or, if you're into Lua:

```lua
messages_foundStickerSets={_='messages.foundStickerSets', hash=int, sets={StickerSetCovered}}

```


