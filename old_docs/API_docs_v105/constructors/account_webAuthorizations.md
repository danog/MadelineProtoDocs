---
title: account.webAuthorizations
description: Telegram login authorizations
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: account.webAuthorizations  
[Back to constructors index](index.md)



Telegram login authorizations

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|authorizations|Array of [WebAuthorization](../types/WebAuthorization.md) | Yes|Authorizations|
|users|Array of [User](../types/User.md) | Yes|Users|



### Type: [account\_WebAuthorizations](../types/account_WebAuthorizations.md)


### Example:

```php
$account_webAuthorizations = ['_' => 'account.webAuthorizations', 'authorizations' => [WebAuthorization, WebAuthorization], 'users' => [User, User]];
```  


Or, if you're into Lua:

```lua
account_webAuthorizations={_='account.webAuthorizations', authorizations={WebAuthorization}, users={User}}

```


