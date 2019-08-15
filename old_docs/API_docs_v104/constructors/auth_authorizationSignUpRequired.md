---
title: auth.authorizationSignUpRequired
description: auth_authorizationSignUpRequired attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: auth.authorizationSignUpRequired  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|terms\_of\_service|[help\_TermsOfService](../types/help_TermsOfService.md) | Optional|



### Type: [auth\_Authorization](../types/auth_Authorization.md)


### Example:

```php
$auth_authorizationSignUpRequired = ['_' => 'auth.authorizationSignUpRequired', 'terms_of_service' => help_TermsOfService];
```  


Or, if you're into Lua:

```lua
auth_authorizationSignUpRequired={_='auth.authorizationSignUpRequired', terms_of_service=help_TermsOfService}

```


