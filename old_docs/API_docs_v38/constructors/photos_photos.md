---
title: photos.photos
description: photos_photos attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: photos.photos  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|photos|Array of [Photo](../types/Photo.md) | Yes|
|users|Array of [User](../types/User.md) | Yes|



### Type: [photos\_Photos](../types/photos_Photos.md)


### Example:

```php
$photos_photos = ['_' => 'photos.photos', 'photos' => [Photo, Photo], 'users' => [User, User]];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "photos.photos", "photos": [Photo], "users": [User]}
```


Or, if you're into Lua:

```lua
photos_photos={_='photos.photos', photos={Photo}, users={User}}

```


