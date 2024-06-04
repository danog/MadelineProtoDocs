---
title: "messages.availableEffects"
description: "messages.availableEffects attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/messages_availableEffects.html
---
# Constructor: messages.availableEffects  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|hash|[int](/API_docs/types/int.html) | Yes|
|effects|Array of [AvailableEffect](/API_docs/types/AvailableEffect.html) | Yes|
|documents|Array of [Document](/API_docs/types/Document.html) | Yes|



### Type: [messages.AvailableEffects](/API_docs/types/messages.AvailableEffects.html)


### Example:

```
$messages_availableEffects = ['_' => 'messages.availableEffects', 'hash' => int, 'effects' => [AvailableEffect, AvailableEffect], 'documents' => [Document, Document]];
```  
