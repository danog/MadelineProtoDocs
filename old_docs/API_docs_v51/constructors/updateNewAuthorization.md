---
title: updateNewAuthorization
description: Update new authorization
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateNewAuthorization  
[Back to constructors index](index.md)



Update new authorization

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|auth\_key\_id|[long](../types/long.md) | Yes|Auth key ID|
|date|[int](../types/int.md) | Yes|Date|
|device|[string](../types/string.md) | Yes|Device|
|location|[string](../types/string.md) | Yes|Location|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateNewAuthorization = ['_' => 'updateNewAuthorization', 'auth_key_id' => long, 'date' => int, 'device' => 'string', 'location' => 'string'];
```  


Or, if you're into Lua:

```lua
updateNewAuthorization={_='updateNewAuthorization', auth_key_id=long, date=int, device='string', location='string'}

```


