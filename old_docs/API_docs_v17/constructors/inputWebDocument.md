---
title: inputWebDocument
description: The document
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputWebDocument  
[Back to constructors index](index.md)



The document

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|url|[string](../types/string.md) | Yes|Remote document URL to be downloaded using the appropriate [method](https://core.telegram.org/api/files)|
|size|[int](../types/int.md) | Yes|Remote file size|
|mime\_type|[string](../types/string.md) | Yes|Mime type|
|attributes|Array of [DocumentAttribute](../types/DocumentAttribute.md) | Yes|Attributes for media types|



### Type: [InputWebDocument](../types/InputWebDocument.md)


### Example:

```php
$inputWebDocument = ['_' => 'inputWebDocument', 'url' => 'string', 'size' => int, 'mime_type' => 'string', 'attributes' => [DocumentAttribute, DocumentAttribute]];
```  


Or, if you're into Lua:

```lua
inputWebDocument={_='inputWebDocument', url='string', size=int, mime_type='string', attributes={DocumentAttribute}}

```


