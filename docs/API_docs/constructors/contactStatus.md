---
title: "contactStatus"
description: "Contact status: online / offline."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: contactStatus  
[Back to constructors index](index.md)



Contact status: online / offline.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|user\_id|[long](../types/long.md) | Yes|
|status|[UserStatus](../types/UserStatus.md) | Optional|Online status|



### Type: [ContactStatus](../types/ContactStatus.md)


### Example:

```php
$contactStatus = ['_' => 'contactStatus', 'user_id' => long, 'status' => UserStatus];
```  


Or, if you're into Lua:

```lua
contactStatus={_='contactStatus', user_id=long, status=UserStatus}

```


