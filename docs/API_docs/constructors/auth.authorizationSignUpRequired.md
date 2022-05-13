---
title: "auth.authorizationSignUpRequired"
description: "An account with this phone number doesn't exist on telegram: the user has to enter basic information and sign up"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/auth_authorizationSignUpRequired.html
---
# Constructor: auth.authorizationSignUpRequired  
[Back to constructors index](/API_docs/constructors/index.html)



An account with this phone number doesn't exist on telegram: the user has to [enter basic information and sign up](https://core.telegram.org/api/auth)

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|terms\_of\_service|[help.TermsOfService](/API_docs/constructors/help.TermsOfService.html) | Optional|Telegram's terms of service: the user must read and accept the terms of service before signing up to telegram|



### Type: [auth.Authorization](/API_docs/types/auth.Authorization.html)


### Example:

```
$auth_authorizationSignUpRequired = ['_' => 'auth.authorizationSignUpRequired', 'terms_of_service' => help.TermsOfService];
```  
