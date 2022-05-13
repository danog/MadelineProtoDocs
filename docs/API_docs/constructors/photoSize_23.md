---
title: "photoSize"
description: "Image description."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: photoSize\_23  
[Back to constructors index](/API_docs/constructors/index.html)



Image description.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|type|[string](/API_docs/types/string.html) | Yes|Thumbnail type|
|location|[FileLocation](/API_docs/types/FileLocation.html) | Yes|
|w|[int](/API_docs/types/int.html) | Yes|Image width|
|h|[int](/API_docs/types/int.html) | Yes|Image height|
|size|[int](/API_docs/types/int.html) | Yes|File size|



### Type: [PhotoSize](/API_docs/types/PhotoSize.html)


### Example:

```
$photoSize_23 = ['_' => 'photoSize', 'type' => 'string', 'location' => FileLocation, 'w' => int, 'h' => int, 'size' => int];
```  
