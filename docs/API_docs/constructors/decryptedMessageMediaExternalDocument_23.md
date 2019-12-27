---
title: decryptedMessageMediaExternalDocument
description: Non-e2e documented forwarded from non-secret chat
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: decryptedMessageMediaExternalDocument\_23  
[Back to constructors index](index.md)



Non-e2e documented forwarded from non-secret chat

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[long](../types/long.md) | Yes|Document ID|
|access\_hash|[long](../types/long.md) | Yes|access hash|
|date|[int](../types/int.md) | Yes|Date|
|mime\_type|[string](../types/string.md) | Yes|Mime type|
|size|[int](../types/int.md) | Yes|Size|
|thumb|[PhotoSize](../types/PhotoSize.md) | Optional|Thumbnail|
|dc\_id|[int](../types/int.md) | Yes|DC ID|
|attributes|Array of [DocumentAttribute](../types/DocumentAttribute.md) | Yes|Attributes|



### Type: [DecryptedMessageMedia](../types/DecryptedMessageMedia.md)


### Example:

```php
$decryptedMessageMediaExternalDocument_23 = ['_' => 'decryptedMessageMediaExternalDocument', 'id' => long, 'access_hash' => long, 'date' => int, 'mime_type' => 'string', 'size' => int, 'thumb' => PhotoSize, 'dc_id' => int, 'attributes' => [DocumentAttribute, DocumentAttribute]];
```  


Or, if you're into Lua:

```lua
decryptedMessageMediaExternalDocument_23={_='decryptedMessageMediaExternalDocument', id=long, access_hash=long, date=int, mime_type='string', size=int, thumb=PhotoSize, dc_id=int, attributes={DocumentAttribute}}

```


