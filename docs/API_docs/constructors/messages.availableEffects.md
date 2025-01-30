---
title: "messages.availableEffects"
description: "The full list of usable animated message effects »."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/messages_availableEffects.html
---
# Constructor: messages.availableEffects  
[Back to constructors index](/API_docs/constructors/index.html)



The full list of usable [animated message effects »](https://core.telegram.org/api/effects).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|hash|[int](/API_docs/types/int.html) | Yes|
|effects|Array of [AvailableEffect](/API_docs/types/AvailableEffect.html) | Yes|Message effects|
|documents|Array of [Document](/API_docs/types/Document.html) | Yes|Documents specified in the `effects` constructors.|



### Type: [messages.AvailableEffects](/API_docs/types/messages.AvailableEffects.html)


### Example:

```
$messages_availableEffects = ['_' => 'messages.availableEffects', 'hash' => int, 'effects' => [AvailableEffect, AvailableEffect], 'documents' => [Document, Document]];
```  
