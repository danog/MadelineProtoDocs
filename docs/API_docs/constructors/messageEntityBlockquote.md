---
title: "messageEntityBlockquote"
description: "Message entity representing a block quote."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageEntityBlockquote  
[Back to constructors index](/API_docs/constructors/index.html)



Message entity representing a block quote.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|offset|[int](/API_docs/types/int.html) | Yes|Offset of message entity within message (in UTF-8 codepoints)|
|length|[int](/API_docs/types/int.html) | Yes|Length of message entity within message (in UTF-8 codepoints)|



### Type: [MessageEntity](/API_docs/types/MessageEntity.html)


### Example:

```
$messageEntityBlockquote = ['_' => 'messageEntityBlockquote', 'offset' => int, 'length' => int];
```  
