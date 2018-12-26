---
title: bind_auth_key_inner
description: Bind auth key inner
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: bind\_auth\_key\_inner  
[Back to constructors index](index.md)



Bind auth key inner

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|nonce|[long](../types/long.md) | Yes|Nonce|
|temp\_auth\_key\_id|[long](../types/long.md) | Yes|Temp auth key ID|
|perm\_auth\_key\_id|[long](../types/long.md) | Yes|Perm auth key ID|
|temp\_session\_id|[long](../types/long.md) | Yes|Temp session ID|
|expires\_at|[int](../types/int.md) | Yes|Expires at|



### Type: [BindAuthKeyInner](../types/BindAuthKeyInner.md)


### Example:

```php
$bind_auth_key_inner = ['_' => 'bind_auth_key_inner', 'nonce' => long, 'temp_auth_key_id' => long, 'perm_auth_key_id' => long, 'temp_session_id' => long, 'expires_at' => int];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "bind_auth_key_inner", "nonce": long, "temp_auth_key_id": long, "perm_auth_key_id": long, "temp_session_id": long, "expires_at": int}
```


Or, if you're into Lua:

```lua
bind_auth_key_inner={_='bind_auth_key_inner', nonce=long, temp_auth_key_id=long, perm_auth_key_id=long, temp_session_id=long, expires_at=int}

```


