---
title: "inputWebDocument"
description: "The document"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputWebDocument  
[Back to constructors index](/API_docs/constructors/index.md)



The document

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|url|[string](/API_docs/types/string.md) | Yes|Remote document URL to be downloaded using the appropriate [method](https://core.telegram.org/api/files)|
|size|[int](/API_docs/types/int.md) | Yes|Remote file size|
|mime\_type|[string](/API_docs/types/string.md) | Yes|Mime type|
|attributes|Array of [DocumentAttribute](/API_docs/types/DocumentAttribute.md) | Yes|Attributes for media types|



### Type: [InputWebDocument](/API_docs/types/InputWebDocument.md)


### Example:

```php
$inputWebDocument = ['_' => 'inputWebDocument', 'url' => 'string', 'size' => int, 'mime_type' => 'string', 'attributes' => [DocumentAttribute, DocumentAttribute]];
```  
