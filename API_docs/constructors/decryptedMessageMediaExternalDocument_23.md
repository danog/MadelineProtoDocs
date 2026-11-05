# decryptedMessageMediaExternalDocument

> Non-e2e documented forwarded from non-secret chat

[Back to constructors index](/API_docs/constructors/index.html)



Non-e2e documented forwarded from non-secret chat

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[long](/API_docs/types/long.html) | Yes|Document ID|
|access\_hash|[long](/API_docs/types/long.html) | Yes|access hash|
|date|[int](/API_docs/types/int.html) | Yes|Date|
|mime\_type|[string](/API_docs/types/string.html) | Yes|Mime type|
|size|[int](/API_docs/types/int.html) | Yes|Size|
|thumb|[PhotoSize](/API_docs/types/PhotoSize.html) | Optional|Thumbnail|
|dc\_id|[int](/API_docs/types/int.html) | Yes|DC ID|
|attributes|Array of [DocumentAttribute](/API_docs/types/DocumentAttribute.html) | Yes|Attributes for media types|



### Type: [DecryptedMessageMedia](/API_docs/types/DecryptedMessageMedia.html)


### Example:

```
$decryptedMessageMediaExternalDocument_23 = ['_' => 'decryptedMessageMediaExternalDocument', 'id' => long, 'access_hash' => long, 'date' => int, 'mime_type' => 'string', 'size' => int, 'thumb' => PhotoSize, 'dc_id' => int, 'attributes' => [DocumentAttribute, DocumentAttribute]];
```
