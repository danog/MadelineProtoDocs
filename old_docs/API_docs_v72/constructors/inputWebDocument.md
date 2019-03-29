---
title: inputWebDocument
description: Web document
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputWebDocument  
[Back to constructors index](index.md)



Web document

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|url|[string](../types/string.md) | Yes|URL|
|size|[int](../types/int.md) | Yes|Size|
|mime\_type|[string](../types/string.md) | Yes|Mime type|
|attributes|Array of [DocumentAttribute](../types/DocumentAttribute.md) | Yes|Attributes|



### Type: [InputWebDocument](../types/InputWebDocument.md)


### Example:

```php
$inputWebDocument = ['_' => 'inputWebDocument', 'url' => 'string', 'size' => int, 'mime_type' => 'string', 'attributes' => [DocumentAttribute, DocumentAttribute]];
```  


Or, if you're into Lua:

```lua
inputWebDocument={_='inputWebDocument', url='string', size=int, mime_type='string', attributes={DocumentAttribute}}

```


