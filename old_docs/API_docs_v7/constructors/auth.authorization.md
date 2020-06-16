---
title: auth.authorization
description: Contains user authorization info.
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/auth_authorization.html
---
# Constructor: auth.authorization  
[Back to constructors index](index.md)



Contains user authorization info.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|user|[User](../types/User.md) | Optional|Info on authorized user|



### Type: [auth.Authorization](../types/auth.Authorization.md)


### Example:

```php
$auth.authorization = ['_' => 'auth.authorization', 'user' => User];
```  


Or, if you're into Lua:

```lua
auth.authorization={_='auth.authorization', user=User}

```


