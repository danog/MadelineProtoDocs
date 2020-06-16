---
title: messages.foundStickerSets
description: Found stickersets
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/messages_foundStickerSets.html
---
# Constructor: messages.foundStickerSets  
[Back to constructors index](index.md)



Found stickersets

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|hash|[int](../types/int.md) | Yes|
|sets|Array of [StickerSetCovered](../types/StickerSetCovered.md) | Yes|Found stickersets|



### Type: [messages.FoundStickerSets](../types/messages.FoundStickerSets.md)


### Example:

```php
$messages.foundStickerSets = ['_' => 'messages.foundStickerSets', 'hash' => int, 'sets' => [StickerSetCovered, StickerSetCovered]];
```  


Or, if you're into Lua:

```lua
messages.foundStickerSets={_='messages.foundStickerSets', hash=int, sets={StickerSetCovered}}

```


