---
title: "userProfilePhoto"
description: "User profile photo."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: userProfilePhoto  
[Back to constructors index](index.md)



User profile photo.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|has\_video|[Bool](../types/Bool.md) | Optional|Whether an [animated profile picture](https://core.telegram.org/api/files#animated-profile-pictures) is available for this user|
|photo\_id|[long](../types/long.md) | Yes|Identifier of the respective photo<br>Parameter added in [Layer 2](https://core.telegram.org/api/layers#layer-2)|
|stripped\_thumb|[bytes](../types/bytes.md) | Optional|
|dc\_id|[int](../types/int.md) | Yes|DC ID where the photo is stored|



### Type: [UserProfilePhoto](../types/UserProfilePhoto.md)


### Example:

```php
$userProfilePhoto = ['_' => 'userProfilePhoto', 'has_video' => Bool, 'photo_id' => long, 'stripped_thumb' => 'bytes', 'dc_id' => int];
```  


Or, if you're into Lua:

```lua
userProfilePhoto={_='userProfilePhoto', has_video=Bool, photo_id=long, stripped_thumb='bytes', dc_id=int}

```


