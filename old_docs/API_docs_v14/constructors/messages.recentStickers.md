---
title: messages.recentStickers
description: Recently used stickers
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/messages_recentStickers.html
---
# Constructor: messages.recentStickers  
[Back to constructors index](index.md)



Recently used stickers

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|hash|[int](../types/int.md) | Yes|
|stickers|Array of [Document](../types/Document.md) | Yes|Recent stickers|



### Type: [messages.RecentStickers](../types/messages.RecentStickers.md)


### Example:

```php
$messages_recentStickers = ['_' => 'messages.recentStickers', 'hash' => int, 'stickers' => [Document, Document]];
```  


Or, if you're into Lua:

```lua
messages_recentStickers={_='messages.recentStickers', hash=int, stickers={Document}}

```


