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
|required\_types|Array of [SecureRequiredType](../types/SecureRequiredType.md) | Yes|Required [Telegram Passport](https://core.telegram.org/passport) documents|
|values|Array of [SecureValue](../types/SecureValue.md) | Yes|Already submitted [Telegram Passport](https://core.telegram.org/passport) documents|
|errors|Array of [SecureValueError](../types/SecureValueError.md) | Yes|[Telegram Passport](https://core.telegram.org/passport) errors|
|users|Array of [User](../types/User.md) | Yes|Info about the bot to which the form will be submitted|
|privacy\_policy\_url|[string](../types/string.md) | Optional|URL of the service's privacy policy|



### Type: [account.AuthorizationForm](../types/account.AuthorizationForm.md)


### Example:

```php
$account.authorizationForm = ['_' => 'account.authorizationForm', 'required_types' => [SecureRequiredType, SecureRequiredType], 'values' => [SecureValue, SecureValue], 'errors' => [SecureValueError, SecureValueError], 'users' => [User, User], 'privacy_policy_url' => 'string'];
```  


Or, if you're into Lua:

```lua
account.authorizationForm={_='account.authorizationForm', required_types={SecureRequiredType}, values={SecureValue}, errors={SecureValueError}, users={User}, privacy_policy_url='string'}

```


