---
title: "auth.sentCodeTypeMissedCall"
description: "The code will be sent via a flash phone call, that will be closed immediately. The last digits of the phone number that calls are the code that must be entered manually by the user."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/auth_sentCodeTypeMissedCall.html
---
# Constructor: auth.sentCodeTypeMissedCall  
[Back to constructors index](/API_docs/constructors/index.html)



The code will be sent via a flash phone call, that will be closed immediately. The last digits of the phone number that calls are the code that must be entered manually by the user.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|prefix|[string](/API_docs/types/string.html) | Yes|Prefix of the phone number from which the call will be made|
|length|[int](/API_docs/types/int.html) | Yes|Length of the verification code|



### Type: [auth.SentCodeType](/API_docs/types/auth.SentCodeType.html)


### Example:

```
$auth_sentCodeTypeMissedCall = ['_' => 'auth.sentCodeTypeMissedCall', 'prefix' => 'string', 'length' => int];
```  
