---
title: "photos.photosSlice"
description: "Incomplete list of photos with auxiliary data."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/photos_photosSlice.html
---
# Constructor: photos.photosSlice  
[Back to constructors index](/API_docs/constructors/index.md)



Incomplete list of photos with auxiliary data.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|count|[int](/API_docs/types/int.md) | Yes|Total number of photos|
|photos|Array of [Photo](/API_docs/types/Photo.md) | Yes|List of photos|
|users|Array of [User](/API_docs/types/User.md) | Yes|List of mentioned users|



### Type: [photos.Photos](/API_docs/types/photos.Photos.md)


### Example:

```php
$photos_photosSlice = ['_' => 'photos.photosSlice', 'count' => int, 'photos' => [Photo, Photo], 'users' => [User, User]];
```  
