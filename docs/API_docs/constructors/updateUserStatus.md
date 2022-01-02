---
title: "updateUserStatus"
description: "Contact status update."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateUserStatus  
[Back to constructors index](index.md)



Contact status update.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|user\_id|[long](../types/long.md) | Yes|
|status|[UserStatus](../types/UserStatus.md) | Optional|New status|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateUserStatus = ['_' => 'updateUserStatus', 'user_id' => long, 'status' => UserStatus];
```  


Or, if you're into Lua:

```lua
updateUserStatus={_='updateUserStatus', user_id=long, status=UserStatus}

```


