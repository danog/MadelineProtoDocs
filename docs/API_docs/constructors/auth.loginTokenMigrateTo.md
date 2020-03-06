---
title: auth.loginTokenMigrateTo
description: auth.loginTokenMigrateTo attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/auth_loginTokenMigrateTo.html
---
# Constructor: auth.loginTokenMigrateTo  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|dc\_id|[int](../types/int.md) | Yes|
|token|[bytes](../types/bytes.md) | Yes|



### Type: [auth.LoginToken](../types/auth.LoginToken.md)


### Example:

```php
$auth.loginTokenMigrateTo = ['_' => 'auth.loginTokenMigrateTo', 'dc_id' => int, 'token' => 'bytes'];
```  


Or, if you're into Lua:

```lua
auth.loginTokenMigrateTo={_='auth.loginTokenMigrateTo', dc_id=int, token='bytes'}

```


