---
title: "auth.sentCodeTypeSetUpEmailRequired"
description: "auth.sentCodeTypeSetUpEmailRequired attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/auth_sentCodeTypeSetUpEmailRequired.html
---
# Constructor: auth.sentCodeTypeSetUpEmailRequired  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|apple\_signin\_allowed|[Bool](/API_docs/types/Bool.html) | Optional|
|google\_signin\_allowed|[Bool](/API_docs/types/Bool.html) | Optional|



### Type: [auth.SentCodeType](/API_docs/types/auth.SentCodeType.html)


### Example:

```
$auth_sentCodeTypeSetUpEmailRequired = ['_' => 'auth.sentCodeTypeSetUpEmailRequired', 'apple_signin_allowed' => Bool, 'google_signin_allowed' => Bool];
```  
