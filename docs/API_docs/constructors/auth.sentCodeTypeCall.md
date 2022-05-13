---
title: "auth.sentCodeTypeCall"
description: "The code will be sent via a phone call: a synthesized voice will tell the user which verification code to input."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/auth_sentCodeTypeCall.html
---
# Constructor: auth.sentCodeTypeCall  
[Back to constructors index](/API_docs/constructors/index.html)



The code will be sent via a phone call: a synthesized voice will tell the user which verification code to input.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|length|[int](/API_docs/types/int.html) | Yes|Length of the verification code|



### Type: [auth.SentCodeType](/API_docs/types/auth.SentCodeType.html)


### Example:

```
$auth_sentCodeTypeCall = ['_' => 'auth.sentCodeTypeCall', 'length' => int];
```  
