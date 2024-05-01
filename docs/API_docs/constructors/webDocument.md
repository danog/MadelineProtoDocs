---
title: "webDocument"
description: "Remote document"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: webDocument  
[Back to constructors index](/API_docs/constructors/index.html)



Remote document

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|url|[string](/API_docs/types/string.html) | Yes|Document URL|
|access\_hash|[long](/API_docs/types/long.html) | Yes|Access hash|
|size|[int](/API_docs/types/int.html) | Yes|File size|
|mime\_type|[string](/API_docs/types/string.html) | Yes|MIME type|
|attributes|Array of [DocumentAttribute](/API_docs/types/DocumentAttribute.html) | Yes|Attributes for media types|



### Type: [WebDocument](/API_docs/types/WebDocument.html)


### Example:

```
$webDocument = ['_' => 'webDocument', 'url' => 'string', 'access_hash' => long, 'size' => int, 'mime_type' => 'string', 'attributes' => [DocumentAttribute, DocumentAttribute]];
```  
