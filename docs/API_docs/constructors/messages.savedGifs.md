---
title: "messages.savedGifs"
description: "Saved gifs"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/messages_savedGifs.html
---
# Constructor: messages.savedGifs  
[Back to constructors index](/API_docs/constructors/index.md)



Saved gifs

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|hash|[long](/API_docs/types/long.md) | Yes|
|gifs|Array of [Document](/API_docs/types/Document.md) | Yes|List of saved gifs|



### Type: [messages.SavedGifs](/API_docs/types/messages.SavedGifs.md)


### Example:

```php
$messages_savedGifs = ['_' => 'messages.savedGifs', 'hash' => long, 'gifs' => [Document, Document]];
```  
