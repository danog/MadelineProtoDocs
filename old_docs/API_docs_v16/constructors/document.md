---
title: document
description: Document
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: document  
[Back to constructors index](index.md)



Document

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[long](../types/long.md) | Yes|Document ID|
|access\_hash|[long](../types/long.md) | Yes|Check sum, dependant on document ID|
|date|[int](../types/int.md) | Yes|Creation date|
|mime\_type|[string](../types/string.md) | Yes|MIME type|
|size|[int](../types/int.md) | Yes|Size|
|thumb|[PhotoSize](../types/PhotoSize.md) | Optional|
|dc\_id|[int](../types/int.md) | Yes|DC ID|
|version|[int](../types/int.md) | Yes|
|attributes|Array of [DocumentAttribute](../types/DocumentAttribute.md) | Yes|Attributes|



### Type: [Document](../types/Document.md)


### Example:

```php
$document = ['_' => 'document', 'id' => long, 'access_hash' => long, 'date' => int, 'mime_type' => 'string', 'size' => int, 'thumb' => PhotoSize, 'dc_id' => int, 'version' => int, 'attributes' => [DocumentAttribute, DocumentAttribute]];
```  


Or, if you're into Lua:

```lua
document={_='document', id=long, access_hash=long, date=int, mime_type='string', size=int, thumb=PhotoSize, dc_id=int, version=int, attributes={DocumentAttribute}}

```


