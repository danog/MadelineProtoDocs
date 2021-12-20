---
title: "messages.savedGifs"
description: "Saved gifs"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/messages_savedGifs.html
---
# Constructor: messages.savedGifs  
[Back to constructors index](index.md)



Saved gifs

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|hash|[long](../types/long.md) | Yes|
|gifs|Array of [Document](../types/Document.md) | Yes|List of saved gifs|



### Type: [messages.SavedGifs](../types/messages.SavedGifs.md)


### Example:

```php
$messages_savedGifs = ['_' => 'messages.savedGifs', 'hash' => long, 'gifs' => [Document, Document]];
```  


Or, if you're into Lua:

```lua
messages_savedGifs={_='messages.savedGifs', hash=long, gifs={Document}}

```


