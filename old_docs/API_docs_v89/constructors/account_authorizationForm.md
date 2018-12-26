---
title: account.authorizationForm
description: Telegram passport authorization form
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: account.authorizationForm  
[Back to constructors index](index.md)



Telegram passport authorization form

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|required\_types|Array of [SecureRequiredType](../types/SecureRequiredType.md) | Yes|Required types|
|values|Array of [SecureValue](../types/SecureValue.md) | Yes|Values|
|errors|Array of [SecureValueError](../types/SecureValueError.md) | Yes|Errors|
|users|Array of [User](../types/User.md) | Yes|Users|
|privacy\_policy\_url|[string](../types/string.md) | Optional|Privacy policy URL|



### Type: [account\_AuthorizationForm](../types/account_AuthorizationForm.md)


### Example:

```php
$account_authorizationForm = ['_' => 'account.authorizationForm', 'required_types' => [SecureRequiredType, SecureRequiredType], 'values' => [SecureValue, SecureValue], 'errors' => [SecureValueError, SecureValueError], 'users' => [User, User], 'privacy_policy_url' => 'string'];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "account.authorizationForm", "required_types": [SecureRequiredType], "values": [SecureValue], "errors": [SecureValueError], "users": [User], "privacy_policy_url": "string"}
```


Or, if you're into Lua:

```lua
account_authorizationForm={_='account.authorizationForm', required_types={SecureRequiredType}, values={SecureValue}, errors={SecureValueError}, users={User}, privacy_policy_url='string'}

```


