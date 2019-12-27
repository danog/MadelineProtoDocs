---
title: auth.authorizationSignUpRequired
description: An account with this phone number doesn't exist on telegram: the user has to [enter basic information and sign up](https://core.telegram.org/api/auth)
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: auth.authorizationSignUpRequired  
[Back to constructors index](index.md)



An account with this phone number doesn't exist on telegram: the user has to [enter basic information and sign up](https://core.telegram.org/api/auth)

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|terms\_of\_service|[help.TermsOfService](../constructors/help.TermsOfService.md) | Optional|Telegram's terms of service: the user must read and accept the terms of service before signing up to telegram|



### Type: [auth.Authorization](../types/auth.Authorization.md)


### Example:

```php
$auth.authorizationSignUpRequired = ['_' => 'auth.authorizationSignUpRequired', 'terms_of_service' => help.TermsOfService];
```  


Or, if you're into Lua:

```lua
auth.authorizationSignUpRequired={_='auth.authorizationSignUpRequired', terms_of_service=help.TermsOfService}

```


