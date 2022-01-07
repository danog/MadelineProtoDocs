---
title: "messageMediaPhoto"
description: "Attached photo."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageMediaPhoto  
[Back to constructors index](/API_docs/constructors/index.md)



Attached photo.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|photo|[Photo](/API_docs/types/Photo.md) | Optional|Photo|
|ttl\_seconds|[int](/API_docs/types/int.md) | Optional|Time to live in seconds of self-destructing photo|



### Type: [MessageMedia](/API_docs/types/MessageMedia.md)


### Example:

```php
$messageMediaPhoto = ['_' => 'messageMediaPhoto', 'photo' => Photo, 'ttl_seconds' => int];
```  
