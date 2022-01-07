---
title: "inputMediaDocument"
description: "Forwarded document"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputMediaDocument  
[Back to constructors index](/API_docs/constructors/index.md)



Forwarded document

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[MessageMedia, Message, Update or InputDocument](/API_docs/types/InputDocument.md) | Optional|The document to be forwarded.|
|ttl\_seconds|[int](/API_docs/types/int.md) | Optional|Time to live of self-destructing document|
|query|[string](/API_docs/types/string.md) | Optional|



### Type: [InputMedia](/API_docs/types/InputMedia.md)


### Example:

```php
$inputMediaDocument = ['_' => 'inputMediaDocument', 'id' => InputDocument, 'ttl_seconds' => int, 'query' => 'string'];
```  
