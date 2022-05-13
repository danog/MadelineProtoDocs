---
title: "messageEntitySpoiler"
description: "Message entity representing a spoiler"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageEntitySpoiler  
[Back to constructors index](/API_docs/constructors/index.html)



Message entity representing a spoiler

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|offset|[int](/API_docs/types/int.html) | Yes|Offset of message entity within message (in UTF-8 codepoints)|
|length|[int](/API_docs/types/int.html) | Yes|Length of message entity within message (in UTF-8 codepoints)|



### Type: [MessageEntity](/API_docs/types/MessageEntity.html)


### Example:

```
$messageEntitySpoiler = ['_' => 'messageEntitySpoiler', 'offset' => int, 'length' => int];
```  
