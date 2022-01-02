---
title: "account.webAuthorizations"
description: "Web authorizations"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/account_webAuthorizations.html
---
# Constructor: account.webAuthorizations  
[Back to constructors index](index.md)



Web authorizations

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|authorizations|Array of [WebAuthorization](../types/WebAuthorization.md) | Yes|Web authorization list|
|users|Array of [User](../types/User.md) | Yes|Users|



### Type: [account.WebAuthorizations](../types/account.WebAuthorizations.md)


### Example:

```php
$account_webAuthorizations = ['_' => 'account.webAuthorizations', 'authorizations' => [WebAuthorization, WebAuthorization], 'users' => [User, User]];
```  


Or, if you're into Lua:

```lua
account_webAuthorizations={_='account.webAuthorizations', authorizations={WebAuthorization}, users={User}}

```


