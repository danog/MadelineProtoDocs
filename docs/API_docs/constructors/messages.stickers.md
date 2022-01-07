---
title: "messages.stickers"
description: "Found stickers"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/messages_stickers.html
---
# Constructor: messages.stickers  
[Back to constructors index](/API_docs/constructors/index.html)



Found stickers

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|hash|[long](/API_docs/types/long.html) | Yes|
|stickers|Array of [Document](/API_docs/types/Document.html) | Yes|Stickers|



### Type: [messages.Stickers](/API_docs/types/messages.Stickers.html)


### Example:

```php
$messages_stickers = ['_' => 'messages.stickers', 'hash' => long, 'stickers' => [Document, Document]];
```  
