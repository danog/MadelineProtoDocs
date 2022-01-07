---
title: "photoCachedSize"
description: "Description of an image and its content."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: photoCachedSize  
[Back to constructors index](/API_docs/constructors/index.md)



Description of an image and its content.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|type|[string](/API_docs/types/string.md) | Yes|Thumbnail type|
|w|[int](/API_docs/types/int.md) | Yes|Image width|
|h|[int](/API_docs/types/int.md) | Yes|Image height|
|bytes|[bytes](/API_docs/types/bytes.md) | Yes|Binary data, file content|



### Type: [PhotoSize](/API_docs/types/PhotoSize.md)


### Example:

```php
$photoCachedSize = ['_' => 'photoCachedSize', 'type' => 'string', 'w' => int, 'h' => int, 'bytes' => 'bytes'];
```  
