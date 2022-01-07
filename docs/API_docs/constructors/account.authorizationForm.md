---
title: "account.authorizationForm"
description: "Telegram Passport authorization form"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/account_authorizationForm.html
---
# Constructor: account.authorizationForm  
[Back to constructors index](/API_docs/constructors/index.md)



[Telegram Passport](https://core.telegram.org/passport) authorization form

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|required\_types|Array of [SecureRequiredType](/API_docs/types/SecureRequiredType.md) | Yes|Required [Telegram Passport](https://core.telegram.org/passport) documents|
|values|Array of [SecureValue](/API_docs/types/SecureValue.md) | Yes|Already submitted [Telegram Passport](https://core.telegram.org/passport) documents|
|errors|Array of [SecureValueError](/API_docs/types/SecureValueError.md) | Yes|[Telegram Passport](https://core.telegram.org/passport) errors|
|users|Array of [User](/API_docs/types/User.md) | Yes|Info about the bot to which the form will be submitted|
|privacy\_policy\_url|[string](/API_docs/types/string.md) | Optional|URL of the service's privacy policy|



### Type: [account.AuthorizationForm](/API_docs/types/account.AuthorizationForm.md)


### Example:

```php
$account_authorizationForm = ['_' => 'account.authorizationForm', 'required_types' => [SecureRequiredType, SecureRequiredType], 'values' => [SecureValue, SecureValue], 'errors' => [SecureValueError, SecureValueError], 'users' => [User, User], 'privacy_policy_url' => 'string'];
```  
