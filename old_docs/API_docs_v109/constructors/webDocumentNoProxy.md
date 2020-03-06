---
title: webDocumentNoProxy
description: Remote document that can be downloaded without [proxying through telegram](https://core.telegram.org/api/files)
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: webDocumentNoProxy  
[Back to constructors index](index.md)



Remote document that can be downloaded without [proxying through telegram](https://core.telegram.org/api/files)

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|url|[string](../types/string.md) | Yes|Document URL|
|size|[int](../types/int.md) | Yes|File size|
|mime\_type|[string](../types/string.md) | Yes|MIME type|
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


