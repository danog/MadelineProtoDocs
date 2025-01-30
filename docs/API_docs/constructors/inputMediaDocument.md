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
|spoiler|[Bool](/API_docs/types/Bool.html) | Optional|Whether this media should be hidden behind a spoiler warning|
|id|[MessageMedia, Message, Update or InputDocument](/API_docs/types/InputDocument.html) | Optional|The document to be forwarded.|
|video\_cover|[MessageMedia, Message, Update or InputPhoto](/API_docs/types/InputPhoto.html) | Optional|
|video\_timestamp|[int](/API_docs/types/int.html) | Optional|
|ttl\_seconds|[int](/API_docs/types/int.html) | Optional|Time to live of self-destructing document|
|query|[string](/API_docs/types/string.html) | Optional|Text query or emoji that was used by the user to find this sticker or GIF: used to improve search result relevance.|



### Type: [InputMedia](/API_docs/types/InputMedia.html)


### Example:

```
$inputMediaDocument = ['_' => 'inputMediaDocument', 'spoiler' => Bool, 'id' => InputDocument, 'video_cover' => InputPhoto, 'video_timestamp' => int, 'ttl_seconds' => int, 'query' => 'string'];
```  
