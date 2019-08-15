---
title: auth.authorizationSignUpRequired
description: Signup is required
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: auth.authorizationSignUpRequired  
[Back to constructors index](index.md)



Signup is required

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|terms\_of\_service|[help\_TermsOfService](../types/help_TermsOfService.md) | Optional|Telegram's Terms of Service|



### Type: [auth\_Authorization](../types/auth_Authorization.md)


### Example:

```php
$auth_authorizationSignUpRequired = ['_' => 'auth.authorizationSignUpRequired', 'terms_of_service' => help_TermsOfService];
```  


Or, if you're into Lua:

```lua
auth_authorizationSignUpRequired={_='auth.authorizationSignUpRequired', terms_of_service=help_TermsOfService}

```


