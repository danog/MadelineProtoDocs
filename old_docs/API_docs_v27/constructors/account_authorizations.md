---
title: account.authorizations
description: Logged-in sessions
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: account.authorizations  
[Back to constructors index](index.md)



Logged-in sessions

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|authorizations|Array of [Authorization](../types/Authorization.md) | Yes|Authorizations|



### Type: [account\_Authorizations](../types/account_Authorizations.md)


### Example:

```php
$account_authorizations = ['_' => 'account.authorizations', 'authorizations' => [Authorization, Authorization]];
```  


Or, if you're into Lua:

```lua
account_authorizations={_='account.authorizations', authorizations={Authorization}}

```


