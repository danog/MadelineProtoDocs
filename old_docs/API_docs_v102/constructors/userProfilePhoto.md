---
title: userProfilePhoto
description: User profile photo
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: userProfilePhoto  
[Back to constructors index](index.md)



User profile photo

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|photo\_id|[long](../types/long.md) | Yes|Photo ID|
|photo\_small|[FileLocation](../types/FileLocation.md) | Yes|Photo small|
|photo\_big|[FileLocation](../types/FileLocation.md) | Yes|Photo big|
|dc\_id|[int](../types/int.md) | Yes|DC ID|



### Type: [UserProfilePhoto](../types/UserProfilePhoto.md)


### Example:

```php
$userProfilePhoto = ['_' => 'userProfilePhoto', 'photo_id' => long, 'photo_small' => FileLocation, 'photo_big' => FileLocation, 'dc_id' => int];
```  


Or, if you're into Lua:

```lua
userProfilePhoto={_='userProfilePhoto', photo_id=long, photo_small=FileLocation, photo_big=FileLocation, dc_id=int}

```


