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
|user\_id|[int](../types/int.md) | Yes|
|date|[int](../types/int.md) | Yes|Creation date|
|file\_name|[string](../types/string.md) | Yes|
|mime\_type|[string](../types/string.md) | Yes|MIME type|
|size|[int](../types/int.md) | Yes|Size|
|thumb|[PhotoSize](../types/PhotoSize.md) | Optional|
|dc\_id|[int](../types/int.md) | Yes|DC ID|



### Type: [Document](../types/Document.md)


### Example:

```php
$document = ['_' => 'document', 'id' => long, 'access_hash' => long, 'user_id' => int, 'date' => int, 'file_name' => 'string', 'mime_type' => 'string', 'size' => int, 'thumb' => PhotoSize, 'dc_id' => int];
```  


Or, if you're into Lua:

```lua
document={_='document', id=long, access_hash=long, user_id=int, date=int, file_name='string', mime_type='string', size=int, thumb=PhotoSize, dc_id=int}

```


