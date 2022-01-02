---
title: "auth.loggedOut"
description: "auth.loggedOut attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/auth_loggedOut.html
---
# Constructor: auth.loggedOut  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|future\_auth\_token|[bytes](../types/bytes.md) | Optional|



### Type: [auth.LoggedOut](../types/auth.LoggedOut.md)


### Example:

```php
$auth_loggedOut = ['_' => 'auth.loggedOut', 'future_auth_token' => 'bytes'];
```  


Or, if you're into Lua:

```lua
auth_loggedOut={_='auth.loggedOut', future_auth_token='bytes'}

```


