---
title: messages.foundGifs
description: Found gifs
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messages.foundGifs  
[Back to constructors index](index.md)



Found gifs

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|next\_offset|[int](../types/int.md) | Yes|Next offset|
|results|Array of [FoundGif](../types/FoundGif.md) | Yes|Results|



### Type: [messages\_FoundGifs](../types/messages_FoundGifs.md)


### Example:

```php
$messages_foundGifs = ['_' => 'messages.foundGifs', 'next_offset' => int, 'results' => [FoundGif, FoundGif]];
```  


Or, if you're into Lua:

```lua
messages_foundGifs={_='messages.foundGifs', next_offset=int, results={FoundGif}}

```


