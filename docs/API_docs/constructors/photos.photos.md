---
title: "photos.photos"
description: "Full list of photos with auxiliary data."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/photos_photos.html
---
# Constructor: photos.photos  
[Back to constructors index](/API_docs/constructors/index.md)



Full list of photos with auxiliary data.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|photos|Array of [Photo](/API_docs/types/Photo.md) | Yes|List of photos|
|users|Array of [User](/API_docs/types/User.md) | Yes|List of mentioned users|



### Type: [photos.Photos](/API_docs/types/photos.Photos.md)


### Example:

```php
$photos_photos = ['_' => 'photos.photos', 'photos' => [Photo, Photo], 'users' => [User, User]];
```  
