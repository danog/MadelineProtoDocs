---
title: updateUserPhoto
description: updateUserPhoto attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateUserPhoto  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|user\_id|[int](../types/int.md) | Yes|
|date|[int](../types/int.md) | Yes|
|photo|[UserProfilePhoto](../types/UserProfilePhoto.md) | Optional|
|previous|[Bool](../types/Bool.md) | Yes|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateUserPhoto = ['_' => 'updateUserPhoto', 'user_id' => int, 'date' => int, 'photo' => UserProfilePhoto, 'previous' => Bool];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "updateUserPhoto", "user_id": int, "date": int, "photo": UserProfilePhoto, "previous": Bool}
```


Or, if you're into Lua:

```lua
updateUserPhoto={_='updateUserPhoto', user_id=int, date=int, photo=UserProfilePhoto, previous=Bool}

```


