---
title: webDocument
description: Web document
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: webDocument  
[Back to constructors index](index.md)



Web document

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|url|[string](../types/string.md) | Yes|URL|
|access\_hash|[long](../types/long.md) | Yes|Access hash|
|size|[int](../types/int.md) | Yes|Size|
|mime\_type|[string](../types/string.md) | Yes|Mime type|
|attributes|Array of [DocumentAttribute](../types/DocumentAttribute.md) | Yes|Attributes|
|dc\_id|[int](../types/int.md) | Yes|DC ID|



### Type: [WebDocument](../types/WebDocument.md)


### Example:

```php
$webDocument = ['_' => 'webDocument', 'url' => 'string', 'access_hash' => long, 'size' => int, 'mime_type' => 'string', 'attributes' => [DocumentAttribute, DocumentAttribute], 'dc_id' => int];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "webDocument", "url": "string", "access_hash": long, "size": int, "mime_type": "string", "attributes": [DocumentAttribute], "dc_id": int}
```


Or, if you're into Lua:

```lua
webDocument={_='webDocument', url='string', access_hash=long, size=int, mime_type='string', attributes={DocumentAttribute}, dc_id=int}

```


