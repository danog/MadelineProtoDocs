---
title: "webDocumentNoProxy"
description: "Remote document that can be downloaded without proxying through telegram"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: webDocumentNoProxy  
[Back to constructors index](/API_docs/constructors/index.md)



Remote document that can be downloaded without [proxying through telegram](https://core.telegram.org/api/files)

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|url|[string](/API_docs/types/string.md) | Yes|Document URL|
|size|[int](/API_docs/types/int.md) | Yes|File size|
|mime\_type|[string](/API_docs/types/string.md) | Yes|MIME type|
|attributes|Array of [DocumentAttribute](/API_docs/types/DocumentAttribute.md) | Yes|Attributes for media types|



### Type: [WebDocument](/API_docs/types/WebDocument.md)


### Example:

```php
$webDocumentNoProxy = ['_' => 'webDocumentNoProxy', 'url' => 'string', 'size' => int, 'mime_type' => 'string', 'attributes' => [DocumentAttribute, DocumentAttribute]];
```  
