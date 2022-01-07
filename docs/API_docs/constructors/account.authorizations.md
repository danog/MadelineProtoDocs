---
title: "account.authorizations"
description: "Logged-in sessions"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/account_authorizations.html
---
# Constructor: account.authorizations  
[Back to constructors index](index.md)



Logged-in sessions

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|authorization\_ttl\_days|[int](../types/int.md) | Yes|
|authorizations|Array of [Authorization](../types/Authorization.md) | Yes|Logged-in sessions|



### Type: [account.Authorizations](../types/account.Authorizations.md)


### Example:

```php
$account_authorizations = ['_' => 'account.authorizations', 'authorization_ttl_days' => int, 'authorizations' => [Authorization, Authorization]];
```  
