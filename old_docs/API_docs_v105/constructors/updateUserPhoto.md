---
title: updateUserPhoto
description: Update user photo
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateUserPhoto  
[Back to constructors index](index.md)



Update user photo

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|user\_id|[int](../types/int.md) | Yes|User ID|
|date|[int](../types/int.md) | Yes|Date|
|photo|[UserProfilePhoto](../types/UserProfilePhoto.md) | Optional|Photo|
|previous|[Bool](../types/Bool.md) | Yes|Previous?|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateUserPhoto = ['_' => 'updateUserPhoto', 'user_id' => int, 'date' => int, 'photo' => UserProfilePhoto, 'previous' => Bool];
```  


Or, if you're into Lua:

```lua
updateUserPhoto={_='updateUserPhoto', user_id=int, date=int, photo=UserProfilePhoto, previous=Bool}

```


