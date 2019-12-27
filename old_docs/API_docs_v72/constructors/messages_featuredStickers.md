---
title: messages.featuredStickers
description: Featured stickersets
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messages.featuredStickers  
[Back to constructors index](index.md)



Featured stickersets

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|hash|[int](../types/int.md) | Yes|[Hash for pagination, for more info click here](https://core.telegram.org/api/offsets#hash-generation)|
|sets|Array of [StickerSetCovered](../types/StickerSetCovered.md) | Yes|Sets|
|unread|Array of [long](../types/long.md) | Yes|Unread|



### Type: [messages\_FeaturedStickers](../types/messages_FeaturedStickers.md)


### Example:

```php
$messages_featuredStickers = ['_' => 'messages.featuredStickers', 'hash' => int, 'sets' => [StickerSetCovered, StickerSetCovered], 'unread' => [long, long]];
```  


Or, if you're into Lua:

```lua
messages_featuredStickers={_='messages.featuredStickers', hash=int, sets={StickerSetCovered}, unread={long}}

```


