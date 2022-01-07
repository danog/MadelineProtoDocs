---
title: "photoSize"
description: "Image description."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: photoSize  
[Back to constructors index](/API_docs/constructors/index.md)



Image description.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|type|[string](/API_docs/types/string.md) | Yes|Thumbnail type|
|w|[int](/API_docs/types/int.md) | Yes|Image width|
|h|[int](/API_docs/types/int.md) | Yes|Image height|
|size|[int](/API_docs/types/int.md) | Yes|File size|



### Type: [PhotoSize](/API_docs/types/PhotoSize.md)


### Example:

```php
$photoSize = ['_' => 'photoSize', 'type' => 'string', 'w' => int, 'h' => int, 'size' => int];
```  
