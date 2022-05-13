---
title: "account.authorizationForm"
description: "Telegram Passport authorization form"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/account_authorizationForm.html
---
# Constructor: account.authorizationForm  
[Back to constructors index](/API_docs/constructors/index.html)



[Telegram Passport](https://core.telegram.org/passport) authorization form

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|required\_types|Array of [SecureRequiredType](/API_docs/types/SecureRequiredType.html) | Yes|Required [Telegram Passport](https://core.telegram.org/passport) documents|
|values|Array of [SecureValue](/API_docs/types/SecureValue.html) | Yes|Already submitted [Telegram Passport](https://core.telegram.org/passport) documents|
|errors|Array of [SecureValueError](/API_docs/types/SecureValueError.html) | Yes|[Telegram Passport](https://core.telegram.org/passport) errors|
|users|Array of [User](/API_docs/types/User.html) | Yes|Info about the bot to which the form will be submitted|
|privacy\_policy\_url|[string](/API_docs/types/string.html) | Optional|URL of the service's privacy policy|



### Type: [account.AuthorizationForm](/API_docs/types/account.AuthorizationForm.html)


### Example:

```
$account_authorizationForm = ['_' => 'account.authorizationForm', 'required_types' => [SecureRequiredType, SecureRequiredType], 'values' => [SecureValue, SecureValue], 'errors' => [SecureValueError, SecureValueError], 'users' => [User, User], 'privacy_policy_url' => 'string'];
```  
