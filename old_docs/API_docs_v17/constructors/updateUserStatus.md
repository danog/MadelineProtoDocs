---
title: updateUserStatus
description: Contact status update.
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateUserStatus  
[Back to constructors index](index.md)



Contact status update.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|user\_id|[int](../types/int.md) | Yes|User identifier|
|status|[UserStatus](../types/UserStatus.md) | Optional|New status|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateUserStatus = ['_' => 'updateUserStatus', 'user_id' => int, 'status' => UserStatus];
```  


Or, if you're into Lua:

```lua
updateUserStatus={_='updateUserStatus', user_id=int, status=UserStatus}

```


