---
title: messages.stickers
description: Found stickers
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messages.stickers  
[Back to constructors index](index.md)



Found stickers

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|hash|[int](../types/int.md) | Yes|[Hash for pagination, for more info click here](https://core.telegram.org/api/offsets#hash-generation)|
|stickers|Array of [Document](../types/Document.md) | Yes|Stickers|



### Type: [messages.Stickers](../types/messages.Stickers.md)


### Example:

```php
$messages.stickers = ['_' => 'messages.stickers', 'hash' => int, 'stickers' => [Document, Document]];
```  


Or, if you're into Lua:

```lua
messages.stickers={_='messages.stickers', hash=int, stickers={Document}}

```


