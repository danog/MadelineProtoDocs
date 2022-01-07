---
title: "inputMediaPhoto"
description: "Forwarded photo"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputMediaPhoto  
[Back to constructors index](index.md)



Forwarded photo

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[MessageMedia, Message, Update or InputPhoto](../types/InputPhoto.md) | Optional|Photo to be forwarded|
|ttl\_seconds|[int](../types/int.md) | Optional|Time to live in seconds of self-destructing photo|



### Type: [InputMedia](../types/InputMedia.md)


### Example:

```php
$inputMediaPhoto = ['_' => 'inputMediaPhoto', 'id' => InputPhoto, 'ttl_seconds' => int];
```  
