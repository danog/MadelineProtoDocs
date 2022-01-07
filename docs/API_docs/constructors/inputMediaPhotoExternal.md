---
title: "inputMediaPhotoExternal"
description: "New photo that will be uploaded by the server using the specified URL"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputMediaPhotoExternal  
[Back to constructors index](/API_docs/constructors/index.md)



New photo that will be uploaded by the server using the specified URL

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|url|[string](/API_docs/types/string.md) | Yes|URL of the photo|
|ttl\_seconds|[int](/API_docs/types/int.md) | Optional|Self-destruct time to live of photo|



### Type: [InputMedia](/API_docs/types/InputMedia.md)


### Example:

```php
$inputMediaPhotoExternal = ['_' => 'inputMediaPhotoExternal', 'url' => 'string', 'ttl_seconds' => int];
```  
