---
title: photos.photos
description: Full list of photos with auxiliary data.
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/photos_photos.html
---
# Constructor: photos.photos  
[Back to constructors index](index.md)



Full list of photos with auxiliary data.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|photos|Array of [Photo](../types/Photo.md) | Yes|Photos|
|users|Array of [User](../types/User.md) | Yes|Users|



### Type: [photos.Photos](../types/photos.Photos.md)


### Example:

```php
$photos.photos = ['_' => 'photos.photos', 'photos' => [Photo, Photo], 'users' => [User, User]];
```  


Or, if you're into Lua:

```lua
photos.photos={_='photos.photos', photos={Photo}, users={User}}

```


