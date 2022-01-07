---
title: "auth.authorization"
description: "Contains user authorization info."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/auth_authorization.html
---
# Constructor: auth.authorization  
[Back to constructors index](/API_docs/constructors/index.md)



Contains user authorization info.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|setup\_password\_required|[Bool](/API_docs/types/Bool.md) | Optional|
|otherwise\_relogin\_days|[int](/API_docs/types/int.md) | Optional|
|tmp\_sessions|[int](/API_docs/types/int.md) | Optional|Temporary [passport](https://core.telegram.org/passport) sessions|
|user|[User](/API_docs/types/User.md) | Optional|Info on authorized user|



### Type: [auth.Authorization](/API_docs/types/auth.Authorization.md)


### Example:

```php
$auth_authorization = ['_' => 'auth.authorization', 'setup_password_required' => Bool, 'otherwise_relogin_days' => int, 'tmp_sessions' => int, 'user' => User];
```  
