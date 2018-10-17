---
title: messages.archivedStickers
description: messages_archivedStickers attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messages.archivedStickers  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|count|[int](../types/int.md) | Yes|
|sets|Array of [StickerSetCovered](../types/StickerSetCovered.md) | Yes|



### Type: [messages\_ArchivedStickers](../types/messages_ArchivedStickers.md)


### Example:

```php
$messages_archivedStickers = ['_' => 'messages.archivedStickers', 'count' => int, 'sets' => [StickerSetCovered, StickerSetCovered]];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "messages.archivedStickers", "count": int, "sets": [StickerSetCovered]}
```


Or, if you're into Lua:

```lua
messages_archivedStickers={_='messages.archivedStickers', count=int, sets={StickerSetCovered}}

```


