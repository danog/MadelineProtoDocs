---
title: "auth.authorization"
description: "Contains user authorization info."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/auth_authorization.html
---
# Constructor: auth.authorization  
[Back to constructors index](/API_docs/constructors/index.html)



Contains user authorization info.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|setup\_password\_required|[Bool](/API_docs/types/Bool.html) | Optional|Suggests the user to set up a 2-step verification password to be able to log in again|
|otherwise\_relogin\_days|[int](/API_docs/types/int.html) | Optional|Iff setup\_password\_required is set and the user declines to set a 2-step verification password, they will be able to log into their account via SMS again only after this many days pass.|
|tmp\_sessions|[int](/API_docs/types/int.html) | Optional|Temporary [passport](https://core.telegram.org/passport) sessions|
|user|[User](/API_docs/types/User.html) | Optional|Info on authorized user|



### Type: [auth.Authorization](/API_docs/types/auth.Authorization.html)


### Example:

```
$auth_authorization = ['_' => 'auth.authorization', 'setup_password_required' => Bool, 'otherwise_relogin_days' => int, 'tmp_sessions' => int, 'user' => User];
```  
