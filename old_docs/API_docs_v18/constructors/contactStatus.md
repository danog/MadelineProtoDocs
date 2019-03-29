---
title: contactStatus
description: Contact status
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: contactStatus  
[Back to constructors index](index.md)



Contact status

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|user\_id|[int](../types/int.md) | Yes|User ID|
|expires|[int](../types/int.md) | Yes|Expires|



### Type: [ContactStatus](../types/ContactStatus.md)


### Example:

```php
$contactStatus = ['_' => 'contactStatus', 'user_id' => int, 'expires' => int];
```  


Or, if you're into Lua:

```lua
contactStatus={_='contactStatus', user_id=int, expires=int}

```


