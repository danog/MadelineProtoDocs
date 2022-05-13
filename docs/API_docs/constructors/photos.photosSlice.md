---
title: "photos.photosSlice"
description: "Incomplete list of photos with auxiliary data."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/photos_photosSlice.html
---
# Constructor: photos.photosSlice  
[Back to constructors index](/API_docs/constructors/index.html)



Incomplete list of photos with auxiliary data.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|count|[int](/API_docs/types/int.html) | Yes|Total number of photos|
|photos|Array of [Photo](/API_docs/types/Photo.html) | Yes|List of photos|
|users|Array of [User](/API_docs/types/User.html) | Yes|List of mentioned users|



### Type: [photos.Photos](/API_docs/types/photos.Photos.html)


### Example:

```
$photos_photosSlice = ['_' => 'photos.photosSlice', 'count' => int, 'photos' => [Photo, Photo], 'users' => [User, User]];
```  
