---
title: "account.emailVerifiedLogin"
description: "The email was verified correctly, and a login code was just sent to it."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/account_emailVerifiedLogin.html
---
# Constructor: account.emailVerifiedLogin  
[Back to constructors index](/API_docs/constructors/index.html)



The email was verified correctly, and a login code was just sent to it.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|email|[string](/API_docs/types/string.html) | Yes|The verified email address.|
|sent\_code|[auth.SentCode](/API_docs/constructors/auth.SentCode.html) | Yes|Info about the sent [login code](https://core.telegram.org/api/auth)|



### Type: [account.EmailVerified](/API_docs/types/account.EmailVerified.html)


### Example:

```
$account_emailVerifiedLogin = ['_' => 'account.emailVerifiedLogin', 'email' => 'string', 'sent_code' => auth.SentCode];
```  
