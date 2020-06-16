---
title: account.authorizations
description: Logged-in sessions
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/account_authorizations.html
---
# Constructor: account.authorizations  
[Back to constructors index](index.md)



Logged-in sessions

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|authorizations|Array of [Authorization](../types/Authorization.md) | Yes|Logged-in sessions|



### Type: [account.Authorizations](../types/account.Authorizations.md)


### Example:

```php
$account.authorizations = ['_' => 'account.authorizations', 'authorizations' => [Authorization, Authorization]];
```  


Or, if you're into Lua:

```lua
account.authorizations={_='account.authorizations', authorizations={Authorization}}

```


