---
title: messages.foundGifs
description: Found GIFs
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/messages_foundGifs.html
---
# Constructor: messages.foundGifs  
[Back to constructors index](index.md)



Found GIFs

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|next\_offset|[int](../types/int.md) | Yes|Next offset to use when trying to [load more results](../methods/messages.searchGifs.md)|
|results|Array of [FoundGif](../types/FoundGif.md) | Yes|Results|



### Type: [messages.FoundGifs](../types/messages.FoundGifs.md)


### Example:

```php
$messages.foundGifs = ['_' => 'messages.foundGifs', 'next_offset' => int, 'results' => [FoundGif, FoundGif]];
```  


Or, if you're into Lua:

```lua
messages.foundGifs={_='messages.foundGifs', next_offset=int, results={FoundGif}}

```


