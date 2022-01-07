---
title: "photos.photo"
description: "Photo with auxiliary data."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/photos_photo.html
---
# Constructor: photos.photo  
[Back to constructors index](index.md)



Photo with auxiliary data.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|photo|[Photo](../types/Photo.md) | Optional|Photo|
|users|Array of [User](../types/User.md) | Yes|Users|



### Type: [photos.Photo](../types/photos.Photo.md)


### Example:

```php
$photos_photo = ['_' => 'photos.photo', 'photo' => Photo, 'users' => [User, User]];
```  
