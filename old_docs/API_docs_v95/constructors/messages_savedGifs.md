---
title: messages.savedGifs
description: Saved gifs
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messages.savedGifs  
[Back to constructors index](index.md)



Saved gifs

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|hash|[int](../types/int.md) | Yes|Hash|
|gifs|Array of [Document](../types/Document.md) | Yes|Gifs|



### Type: [messages\_SavedGifs](../types/messages_SavedGifs.md)


### Example:

```php
$messages_savedGifs = ['_' => 'messages.savedGifs', 'hash' => int, 'gifs' => [Document, Document]];
```  


Or, if you're into Lua:

```lua
messages_savedGifs={_='messages.savedGifs', hash=int, gifs={Document}}

```


