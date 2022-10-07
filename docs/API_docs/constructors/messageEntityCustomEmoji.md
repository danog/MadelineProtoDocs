---
title: "messageEntityCustomEmoji"
description: "Represents a custom emoji"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageEntityCustomEmoji  
[Back to constructors index](/API_docs/constructors/index.html)



Represents a custom emoji

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|offset|[int](/API_docs/types/int.html) | Yes|Offset of message entity within message (in [UTF-16 code units](https://core.telegram.org/api/entities#entity-length))|
|length|[int](/API_docs/types/int.html) | Yes|Length of message entity within message (in [UTF-16 code units](https://core.telegram.org/api/entities#entity-length))|
|document\_id|[long](/API_docs/types/long.html) | Yes|Document ID of the [custom emoji](https://core.telegram.org/api/custom-emoji), use [messages.getCustomEmojiDocuments](../methods/messages.getCustomEmojiDocuments.html) to fetch the emoji animation and the actual emoji it represents.|



### Type: [MessageEntity](/API_docs/types/MessageEntity.html)


### Example:

```
$messageEntityCustomEmoji = ['_' => 'messageEntityCustomEmoji', 'offset' => int, 'length' => int, 'document_id' => long];
```  
