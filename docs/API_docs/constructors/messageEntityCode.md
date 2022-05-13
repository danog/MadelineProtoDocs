---
title: "messageEntityCode"
description: "Message entity representing a codeblock."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageEntityCode  
[Back to constructors index](/API_docs/constructors/index.html)



Message entity representing a `codeblock`.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|offset|[int](/API_docs/types/int.html) | Yes|Offset of message entity within message (in UTF-8 codepoints)|
|length|[int](/API_docs/types/int.html) | Yes|Length of message entity within message (in UTF-8 codepoints)|



### Type: [MessageEntity](/API_docs/types/MessageEntity.html)


### Example:

```
$messageEntityCode = ['_' => 'messageEntityCode', 'offset' => int, 'length' => int];
```  
