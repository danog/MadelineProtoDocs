---
title: messages.featuredStickers
description: Featured stickers
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messages.featuredStickers  
[Back to constructors index](index.md)



Featured stickers

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|hash|[int](../types/int.md) | Yes|Hash|
|sets|Array of [StickerSetCovered](../types/StickerSetCovered.md) | Yes|Sets|
|unread|Array of [long](../types/long.md) | Yes|Unread|



### Type: [messages\_FeaturedStickers](../types/messages_FeaturedStickers.md)


### Example:

```php
$messages_featuredStickers = ['_' => 'messages.featuredStickers', 'hash' => int, 'sets' => [StickerSetCovered, StickerSetCovered], 'unread' => [long, long]];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "messages.featuredStickers", "hash": int, "sets": [StickerSetCovered], "unread": [long]}
```


Or, if you're into Lua:

```lua
messages_featuredStickers={_='messages.featuredStickers', hash=int, sets={StickerSetCovered}, unread={long}}

```


