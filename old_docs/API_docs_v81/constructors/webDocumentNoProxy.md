---
title: webDocumentNoProxy
description: Web document no proxy
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: webDocumentNoProxy  
[Back to constructors index](index.md)



Web document no proxy

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|url|[string](../types/string.md) | Yes|URL|
|size|[int](../types/int.md) | Yes|Size|
|mime\_type|[string](../types/string.md) | Yes|Mime type|
|attributes|Array of [DocumentAttribute](../types/DocumentAttribute.md) | Yes|Attributes|



### Type: [WebDocument](../types/WebDocument.md)


### Example:

```php
$webDocumentNoProxy = ['_' => 'webDocumentNoProxy', 'url' => 'string', 'size' => int, 'mime_type' => 'string', 'attributes' => [DocumentAttribute, DocumentAttribute]];
```  


Or, if you're into Lua:

```lua
webDocumentNoProxy={_='webDocumentNoProxy', url='string', size=int, mime_type='string', attributes={DocumentAttribute}}

```


