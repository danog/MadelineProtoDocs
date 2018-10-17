---
title: photos.photo
description: photos_photo attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: photos.photo  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|photo|[Photo](../types/Photo.md) | Optional|
|users|Array of [User](../types/User.md) | Yes|



### Type: [photos\_Photo](../types/photos_Photo.md)


### Example:

```php
$photos_photo = ['_' => 'photos.photo', 'photo' => Photo, 'users' => [User, User]];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "photos.photo", "photo": Photo, "users": [User]}
```


Or, if you're into Lua:

```lua
photos_photo={_='photos.photo', photo=Photo, users={User}}

```


