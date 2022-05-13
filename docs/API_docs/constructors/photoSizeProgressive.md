---
title: "photoSizeProgressive"
description: "Progressively encoded photosize"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: photoSizeProgressive  
[Back to constructors index](/API_docs/constructors/index.html)



Progressively encoded photosize

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|type|[string](/API_docs/types/string.html) | Yes|Photosize type|
|w|[int](/API_docs/types/int.html) | Yes|Photo width|
|h|[int](/API_docs/types/int.html) | Yes|Photo height|
|sizes|Array of [int](/API_docs/types/int.html) | Yes|Sizes of progressive JPEG file prefixes, which can be used to preliminarily show the image.|



### Type: [PhotoSize](/API_docs/types/PhotoSize.html)


### Example:

```
$photoSizeProgressive = ['_' => 'photoSizeProgressive', 'type' => 'string', 'w' => int, 'h' => int, 'sizes' => [int, int]];
```  
