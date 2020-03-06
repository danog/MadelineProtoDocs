---
title: webDocument
description: Remote document
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: webDocument  
[Back to constructors index](index.md)



Remote document

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|url|[string](../types/string.md) | Yes|Document URL|
|access\_hash|[long](../types/long.md) | Yes|Access hash|
|size|[int](../types/int.md) | Yes|File size|
|mime\_type|[string](../types/string.md) | Yes|MIME type|
|attributes|Array of [DocumentAttribute](../types/DocumentAttribute.md) | Yes|Attributes|



### Type: [WebDocument](../types/WebDocument.md)


### Example:

```php
$webDocument = ['_' => 'webDocument', 'url' => 'string', 'access_hash' => long, 'size' => int, 'mime_type' => 'string', 'attributes' => [DocumentAttribute, DocumentAttribute]];
```  


Or, if you're into Lua:

```lua
webDocument={_='webDocument', url='string', access_hash=long, size=int, mime_type='string', attributes={DocumentAttribute}}

```


