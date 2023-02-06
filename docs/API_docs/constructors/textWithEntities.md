---
title: "textWithEntities"
description: "textWithEntities attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: textWithEntities  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|text|[string](/API_docs/types/string.html) | Yes|
|entities|Array of [MessageEntity](/API_docs/types/MessageEntity.html) | Yes|



### Type: [TextWithEntities](/API_docs/types/TextWithEntities.html)


### Example:

```
$textWithEntities = ['_' => 'textWithEntities', 'text' => 'string', 'entities' => [MessageEntity, MessageEntity]];
```  
