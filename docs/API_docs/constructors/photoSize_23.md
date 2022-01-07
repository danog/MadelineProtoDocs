---
title: "photoSize"
description: "Image description."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: photoSize\_23  
[Back to constructors index](/API_docs/constructors/index.md)



Image description.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|type|[string](/API_docs/types/string.md) | Yes|Thumbnail type|
|location|[FileLocation](/API_docs/types/FileLocation.md) | Yes|File location|
|w|[int](/API_docs/types/int.md) | Yes|Image width|
|h|[int](/API_docs/types/int.md) | Yes|Image height|
|size|[int](/API_docs/types/int.md) | Yes|File size|



### Type: [PhotoSize](/API_docs/types/PhotoSize.md)


### Example:

```php
$photoSize_23 = ['_' => 'photoSize', 'type' => 'string', 'location' => FileLocation, 'w' => int, 'h' => int, 'size' => int];
```  
