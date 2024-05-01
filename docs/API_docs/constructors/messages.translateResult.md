---
title: "messages.translateResult"
description: "Translated text with entities"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/messages_translateResult.html
---
# Constructor: messages.translateResult  
[Back to constructors index](/API_docs/constructors/index.html)



Translated text with [entities](https://core.telegram.org/api/entities)

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|result|Array of [TextWithEntities](/API_docs/types/TextWithEntities.html) | Yes|Text+[entities](https://core.telegram.org/api/entities), for each input message.|



### Type: [messages.TranslatedText](/API_docs/types/messages.TranslatedText.html)


### Example:

```
$messages_translateResult = ['_' => 'messages.translateResult', 'result' => [TextWithEntities, TextWithEntities]];
```  
