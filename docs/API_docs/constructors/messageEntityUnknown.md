---
title: "messageEntityUnknown"
description: "Unknown message entity"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageEntityUnknown  
[Back to constructors index](/API_docs/constructors/index.html)



Unknown message entity

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|offset|[int](/API_docs/types/int.html) | Yes|Offset of message entity within message (in UTF-8 codepoints)|
|length|[int](/API_docs/types/int.html) | Yes|Length of message entity within message (in UTF-8 codepoints)|



### Type: [MessageEntity](/API_docs/types/MessageEntity.html)


### Example:

```
$messageEntityUnknown = ['_' => 'messageEntityUnknown', 'offset' => int, 'length' => int];
```  
