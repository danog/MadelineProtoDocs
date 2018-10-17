---
title: messages.foundStickerSets
description: messages_foundStickerSets attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messages.foundStickerSets  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|hash|[int](../types/int.md) | Yes|
|sets|Array of [StickerSetCovered](../types/StickerSetCovered.md) | Yes|



### Type: [messages\_FoundStickerSets](../types/messages_FoundStickerSets.md)


### Example:

```php
$messages_foundStickerSets = ['_' => 'messages.foundStickerSets', 'hash' => int, 'sets' => [StickerSetCovered, StickerSetCovered]];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "messages.foundStickerSets", "hash": int, "sets": [StickerSetCovered]}
```


Or, if you're into Lua:

```lua
messages_foundStickerSets={_='messages.foundStickerSets', hash=int, sets={StickerSetCovered}}

```


