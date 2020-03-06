---
title: messages.featuredStickers
description: Featured stickersets
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/messages_featuredStickers.html
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



### Type: [messages.FeaturedStickers](../types/messages.FeaturedStickers.md)


### Example:

```php
$messages.featuredStickers = ['_' => 'messages.featuredStickers', 'hash' => int, 'sets' => [StickerSetCovered, StickerSetCovered], 'unread' => [long, long]];
```  


Or, if you're into Lua:

```lua
messages.featuredStickers={_='messages.featuredStickers', hash=int, sets={StickerSetCovered}, unread={long}}

```


