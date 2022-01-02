---
title: "photos.photosSlice"
description: "Incomplete list of photos with auxiliary data."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/photos_photosSlice.html
---
# Constructor: photos.photosSlice  
[Back to constructors index](index.md)



Incomplete list of photos with auxiliary data.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|count|[int](../types/int.md) | Yes|Total number of photos|
|photos|Array of [Photo](../types/Photo.md) | Yes|List of photos|
|users|Array of [User](../types/User.md) | Yes|List of mentioned users|



### Type: [photos.Photos](../types/photos.Photos.md)


### Example:

```php
$photos_photosSlice = ['_' => 'photos.photosSlice', 'count' => int, 'photos' => [Photo, Photo], 'users' => [User, User]];
```  


Or, if you're into Lua:

```lua
photos_photosSlice={_='photos.photosSlice', count=int, photos={Photo}, users={User}}

```


