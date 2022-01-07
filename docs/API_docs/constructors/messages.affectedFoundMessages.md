---
title: "messages.affectedFoundMessages"
description: "messages.affectedFoundMessages attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/messages_affectedFoundMessages.html
---
# Constructor: messages.affectedFoundMessages  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|pts|[int](/API_docs/types/int.html) | Yes|
|pts\_count|[int](/API_docs/types/int.html) | Yes|
|offset|[int](/API_docs/types/int.html) | Yes|
|messages|Array of [int](/API_docs/types/int.html) | Yes|



### Type: [messages.AffectedFoundMessages](/API_docs/types/messages.AffectedFoundMessages.html)


### Example:

```php
$messages_affectedFoundMessages = ['_' => 'messages.affectedFoundMessages', 'pts' => int, 'pts_count' => int, 'offset' => int, 'messages' => [int, int]];
```  
