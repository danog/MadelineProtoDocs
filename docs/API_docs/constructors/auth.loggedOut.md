---
title: "auth.loggedOut"
description: "Logout token » to be used on subsequent authorizations"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/auth_loggedOut.html
---
# Constructor: auth.loggedOut  
[Back to constructors index](/API_docs/constructors/index.html)



[Logout token »](https://core.telegram.org/api/auth#logout-tokens) to be used on subsequent authorizations

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|future\_auth\_token|[bytes](/API_docs/types/bytes.html) | Optional|[Logout token »](https://core.telegram.org/api/auth#logout-tokens) to be used on subsequent authorizations|



### Type: [auth.LoggedOut](/API_docs/types/auth.LoggedOut.html)


### Example:

```
$auth_loggedOut = ['_' => 'auth.loggedOut', 'future_auth_token' => 'bytes'];
```  
