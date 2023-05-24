---
title: "textWithEntities"
description: "Styled text with message entities"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: textWithEntities  
[Back to constructors index](/API_docs/constructors/index.html)



Styled text with [message entities](https://core.telegram.org/api/entities)

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|text|[string](/API_docs/types/string.html) | Yes|Text|
|entities|Array of [MessageEntity](/API_docs/types/MessageEntity.html) | Yes|[Message entities for styled text](https://core.telegram.org/api/entities)|



### Type: [TextWithEntities](/API_docs/types/TextWithEntities.html)


### Example:

```
$textWithEntities = ['_' => 'textWithEntities', 'text' => 'string', 'entities' => [MessageEntity, MessageEntity]];
```  
