---
title: "photoCachedSize"
description: "Description of an image and its content."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: photoCachedSize  
[Back to constructors index](index.md)



Description of an image and its content.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|type|[string](../types/string.md) | Yes|Thumbnail type|
|w|[int](../types/int.md) | Yes|Image width|
|h|[int](../types/int.md) | Yes|Image height|
|bytes|[bytes](../types/bytes.md) | Yes|Binary data, file content|



### Type: [PhotoSize](../types/PhotoSize.md)


### Example:

```php
$photoCachedSize = ['_' => 'photoCachedSize', 'type' => 'string', 'w' => int, 'h' => int, 'bytes' => 'bytes'];
```  
