---
title: account.authorizationForm
description: [Telegram Passport](https://core.telegram.org/passport) authorization form
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/account_authorizationForm.html
---
# Constructor: account.authorizationForm  
[Back to constructors index](index.md)



[Telegram Passport](https://core.telegram.org/passport) authorization form

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|selfie\_required|[Bool](../types/Bool.md) | Optional|Selfie required?|
|required\_types|Array of [SecureValueType](../types/SecureValueType.md) | Yes|Required types|
|values|Array of [SecureValue](../types/SecureValue.md) | Yes|Values|
|errors|Array of [SecureValueError](../types/SecureValueError.md) | Yes|Errors|
|users|Array of [User](../types/User.md) | Yes|Users|
|privacy\_policy\_url|[string](../types/string.md) | Optional|URL of the service's privacy policy|



### Type: [account.AuthorizationForm](../types/account.AuthorizationForm.md)


### Example:

```php
$account.authorizationForm = ['_' => 'account.authorizationForm', 'selfie_required' => Bool, 'required_types' => [SecureValueType, SecureValueType], 'values' => [SecureValue, SecureValue], 'errors' => [SecureValueError, SecureValueError], 'users' => [User, User], 'privacy_policy_url' => 'string'];
```  


Or, if you're into Lua:

```lua
account.authorizationForm={_='account.authorizationForm', selfie_required=Bool, required_types={SecureValueType}, values={SecureValue}, errors={SecureValueError}, users={User}, privacy_policy_url='string'}

```


