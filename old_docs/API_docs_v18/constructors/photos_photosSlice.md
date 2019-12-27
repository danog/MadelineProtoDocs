---
title: photos.photosSlice
description: Incomplete list of photos with auxiliary data.
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: photos.photosSlice  
[Back to constructors index](index.md)



Incomplete list of photos with auxiliary data.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|count|[int](../types/int.md) | Yes|Total number of photos|
|photos|Array of [Photo](../types/Photo.md) | Yes|Photos|
|users|Array of [User](../types/User.md) | Yes|Users|



### Type: [photos\_Photos](../types/photos_Photos.md)


### Example:

```php
$photos_photosSlice = ['_' => 'photos.photosSlice', 'count' => int, 'photos' => [Photo, Photo], 'users' => [User, User]];
```  


Or, if you're into Lua:

```lua
photos_photosSlice={_='photos.photosSlice', count=int, photos={Photo}, users={User}}

```


