---
title: "auth.sentCode"
description: "Contains info about a sent verification code."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/auth_sentCode.html
---
# Constructor: auth.sentCode  
[Back to constructors index](/API_docs/constructors/index.html)



Contains info about a sent verification code.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|type|[auth.SentCodeType](/API_docs/constructors/auth.SentCodeType.html) | Yes|Phone code type|
|phone\_code\_hash|[string](/API_docs/types/string.html) | Yes|Phone code hash, to be stored and later re-used with [auth.signIn](../methods/auth.signIn.html)|
|next\_type|[auth.CodeType](/API_docs/constructors/auth.CodeType.html) | Optional|Phone code type that will be sent next, if the phone code is not received within `timeout` seconds: to send it use [auth.resendCode](../methods/auth.resendCode.html)|
|timeout|[int](/API_docs/types/int.html) | Optional|Timeout for reception of the phone code|



### Type: [auth.SentCode](/API_docs/types/auth.SentCode.html)


### Example:

```
$auth_sentCode = ['_' => 'auth.sentCode', 'type' => auth.SentCodeType, 'phone_code_hash' => 'string', 'next_type' => auth.CodeType, 'timeout' => int];
```  
