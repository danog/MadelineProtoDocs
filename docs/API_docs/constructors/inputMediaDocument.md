---
title: "inputMediaDocument"
description: "Forwarded document"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputMediaDocument  
[Back to constructors index](/API_docs/constructors/index.html)



Forwarded document

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[MessageMedia, Message, Update or InputDocument](/API_docs/types/InputDocument.html) | Optional|The document to be forwarded.|
|ttl\_seconds|[int](/API_docs/types/int.html) | Optional|Time to live of self-destructing document|
|query|[string](/API_docs/types/string.html) | Optional|Text query or emoji that was used by the user to find this sticker or GIF: used to improve search result relevance.|



### Type: [InputMedia](/API_docs/types/InputMedia.html)


### Example:

```
$inputMediaDocument = ['_' => 'inputMediaDocument', 'id' => InputDocument, 'ttl_seconds' => int, 'query' => 'string'];
```  
