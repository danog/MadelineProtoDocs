---
title: messages.foundStickerSets
description: Found stickersets
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messages.foundStickerSets  
[Back to constructors index](index.md)



Found stickersets

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|hash|[int](../types/int.md) | Yes|[Hash for pagination, for more info click here](https://core.telegram.org/api/offsets#hash-generation)|
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


