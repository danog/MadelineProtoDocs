---
title: "account.sentEmailCode"
description: "The sent email code"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/account_sentEmailCode.html
---
# Constructor: account.sentEmailCode  
[Back to constructors index](/API_docs/constructors/index.md)



The sent email code

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|email\_pattern|[string](/API_docs/types/string.md) | Yes|The email (to which the code was sent) must match this [pattern](https://core.telegram.org/api/pattern)|
|length|[int](/API_docs/types/int.md) | Yes|The length of the verification code|



### Type: [account.SentEmailCode](/API_docs/types/account.SentEmailCode.md)


### Example:

```php
$account_sentEmailCode = ['_' => 'account.sentEmailCode', 'email_pattern' => 'string', 'length' => int];
```  
