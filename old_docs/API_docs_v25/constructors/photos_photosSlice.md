---
title: photos.photosSlice
description: photos_photosSlice attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: photos.photosSlice  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|count|[int](../types/int.md) | Yes|
|photos|Array of [Photo](../types/Photo.md) | Yes|
|users|Array of [User](../types/User.md) | Yes|



### Type: [photos\_Photos](../types/photos_Photos.md)


### Example:

```php
$photos_photosSlice = ['_' => 'photos.photosSlice', 'count' => int, 'photos' => [Photo, Photo], 'users' => [User, User]];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "photos.photosSlice", "count": int, "photos": [Photo], "users": [User]}
```


Or, if you're into Lua:

```lua
photos_photosSlice={_='photos.photosSlice', count=int, photos={Photo}, users={User}}

```


