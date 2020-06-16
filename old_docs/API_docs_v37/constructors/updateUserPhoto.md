---
title: updateUserPhoto
description: Change of contact's profile photo.
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateUserPhoto  
[Back to constructors index](index.md)



Change of contact's profile photo.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|user\_id|[int](../types/int.md) | Yes|User identifier|
|date|[int](../types/int.md) | Yes|Date of photo update.<br>Parameter was added in [second layer](?layer=2).|
|photo|[UserProfilePhoto](../types/UserProfilePhoto.md) | Optional|New profile photo|
|previous|[Bool](../types/Bool.md) | Yes|([boolTrue](../constructors/boolTrue.md)), if one of the previously used photos is set a profile photo.<br>Parameter was added in [second layer](?layer=2).|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateUserPhoto = ['_' => 'updateUserPhoto', 'user_id' => int, 'date' => int, 'photo' => UserProfilePhoto, 'previous' => Bool];
```  


Or, if you're into Lua:

```lua
updateUserPhoto={_='updateUserPhoto', user_id=int, date=int, photo=UserProfilePhoto, previous=Bool}

```


