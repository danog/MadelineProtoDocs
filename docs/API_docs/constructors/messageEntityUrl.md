---
title: "messageEntityUrl"
description: "Message entity representing an in-text url: https://google.com; for text urls, use messageEntityTextUrl."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageEntityUrl  
[Back to constructors index](/API_docs/constructors/index.html)



Message entity representing an in-text url: <https://google.com>; for [text urls](https://google.com), use [messageEntityTextUrl](../constructors/messageEntityTextUrl.html).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|offset|[int](/API_docs/types/int.html) | Yes|Offset of message entity within message (in UTF-8 codepoints)|
|length|[int](/API_docs/types/int.html) | Yes|Length of message entity within message (in UTF-8 codepoints)|



### Type: [MessageEntity](/API_docs/types/MessageEntity.html)


### Example:

```
$messageEntityUrl = ['_' => 'messageEntityUrl', 'offset' => int, 'length' => int];
```  
