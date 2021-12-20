---
title: "auth.loginTokenMigrateTo"
description: "Repeat the query to the specified DC"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/auth_loginTokenMigrateTo.html
---
# Constructor: auth.loginTokenMigrateTo  
[Back to constructors index](index.md)



Repeat the query to the specified DC

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|dc\_id|[int](../types/int.md) | Yes|DC ID|
|token|[bytes](../types/bytes.md) | Yes|Token to use for login|



### Type: [auth.LoginToken](../types/auth.LoginToken.md)


### Example:

```php
$auth_loginTokenMigrateTo = ['_' => 'auth.loginTokenMigrateTo', 'dc_id' => int, 'token' => 'bytes'];
```  


Or, if you're into Lua:

```lua
auth_loginTokenMigrateTo={_='auth.loginTokenMigrateTo', dc_id=int, token='bytes'}

```


