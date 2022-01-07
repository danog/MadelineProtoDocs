---
title: "decryptedMessageMediaExternalDocument"
description: "Non-e2e documented forwarded from non-secret chat"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: decryptedMessageMediaExternalDocument\_23  
[Back to constructors index](/API_docs/constructors/index.md)



Non-e2e documented forwarded from non-secret chat

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[long](/API_docs/types/long.md) | Yes|Document ID|
|access\_hash|[long](/API_docs/types/long.md) | Yes|access hash|
|date|[int](/API_docs/types/int.md) | Yes|Date|
|mime\_type|[string](/API_docs/types/string.md) | Yes|Mime type|
|size|[int](/API_docs/types/int.md) | Yes|Size|
|thumb|[PhotoSize](/API_docs/types/PhotoSize.md) | Optional|Thumbnail|
|dc\_id|[int](/API_docs/types/int.md) | Yes|DC ID|
|attributes|Array of [DocumentAttribute](/API_docs/types/DocumentAttribute.md) | Yes|Attributes for media types|



### Type: [DecryptedMessageMedia](/API_docs/types/DecryptedMessageMedia.md)


### Example:

```php
$decryptedMessageMediaExternalDocument_23 = ['_' => 'decryptedMessageMediaExternalDocument', 'id' => long, 'access_hash' => long, 'date' => int, 'mime_type' => 'string', 'size' => int, 'thumb' => PhotoSize, 'dc_id' => int, 'attributes' => [DocumentAttribute, DocumentAttribute]];
```  
