---
title: "auth.sentCodeTypeEmailCode"
description: "auth.sentCodeTypeEmailCode attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/auth_sentCodeTypeEmailCode.html
---
# Constructor: auth.sentCodeTypeEmailCode  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|apple\_signin\_allowed|[Bool](/API_docs/types/Bool.html) | Optional|
|google\_signin\_allowed|[Bool](/API_docs/types/Bool.html) | Optional|
|email\_pattern|[string](/API_docs/types/string.html) | Yes|
|length|[int](/API_docs/types/int.html) | Yes|
|reset\_available\_period|[int](/API_docs/types/int.html) | Optional|
|reset\_pending\_date|[int](/API_docs/types/int.html) | Optional|



### Type: [auth.SentCodeType](/API_docs/types/auth.SentCodeType.html)


### Example:

```
$auth_sentCodeTypeEmailCode = ['_' => 'auth.sentCodeTypeEmailCode', 'apple_signin_allowed' => Bool, 'google_signin_allowed' => Bool, 'email_pattern' => 'string', 'length' => int, 'reset_available_period' => int, 'reset_pending_date' => int];
```  
