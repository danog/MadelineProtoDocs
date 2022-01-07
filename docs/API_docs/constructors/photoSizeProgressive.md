---
title: "photoSizeProgressive"
description: "Progressively encoded photosize"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: photoSizeProgressive  
[Back to constructors index](/API_docs/constructors/index.md)



Progressively encoded photosize

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|type|[string](/API_docs/types/string.md) | Yes|Photosize type|
|w|[int](/API_docs/types/int.md) | Yes|Photo width|
|h|[int](/API_docs/types/int.md) | Yes|Photo height|
|sizes|Array of [int](/API_docs/types/int.md) | Yes|Sizes of progressive JPEG file prefixes, which can be used to preliminarily show the image.|



### Type: [PhotoSize](/API_docs/types/PhotoSize.md)


### Example:

```php
$photoSizeProgressive = ['_' => 'photoSizeProgressive', 'type' => 'string', 'w' => int, 'h' => int, 'sizes' => [int, int]];
```  
