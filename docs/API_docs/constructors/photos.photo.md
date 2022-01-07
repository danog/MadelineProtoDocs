---
title: "photos.photo"
description: "Photo with auxiliary data."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/photos_photo.html
---
# Constructor: photos.photo  
[Back to constructors index](/API_docs/constructors/index.md)



Photo with auxiliary data.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|photo|[Photo](/API_docs/types/Photo.md) | Optional|Photo|
|users|Array of [User](/API_docs/types/User.md) | Yes|Users|



### Type: [photos.Photo](/API_docs/types/photos.Photo.md)


### Example:

```php
$photos_photo = ['_' => 'photos.photo', 'photo' => Photo, 'users' => [User, User]];
```  
