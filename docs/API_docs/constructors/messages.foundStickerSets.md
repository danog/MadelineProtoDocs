---
title: "messages.foundStickerSets"
description: "Found stickersets"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/messages_foundStickerSets.html
---
# Constructor: messages.foundStickerSets  
[Back to constructors index](index.md)



Found stickersets

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|hash|[long](../types/long.md) | Yes|
|sets|Array of [StickerSetCovered](../types/StickerSetCovered.md) | Yes|Found stickersets|



### Type: [messages.FoundStickerSets](../types/messages.FoundStickerSets.md)


### Example:

```php
$messages_foundStickerSets = ['_' => 'messages.foundStickerSets', 'hash' => long, 'sets' => [StickerSetCovered, StickerSetCovered]];
```  


Or, if you're into Lua:

```lua
messages_foundStickerSets={_='messages.foundStickerSets', hash=long, sets={StickerSetCovered}}

```


