---
title: "auth.sentCodePaymentRequired"
description: "auth.sentCodePaymentRequired attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/auth_sentCodePaymentRequired.html
---
# Constructor: auth.sentCodePaymentRequired  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|store\_product|[string](/API_docs/types/string.html) | Yes|
|phone\_code\_hash|[string](/API_docs/types/string.html) | Yes|
|support\_email\_address|[string](/API_docs/types/string.html) | Yes|
|support\_email\_subject|[string](/API_docs/types/string.html) | Yes|



### Type: [auth.SentCode](/API_docs/types/auth.SentCode.html)


### Example:

```
$auth_sentCodePaymentRequired = ['_' => 'auth.sentCodePaymentRequired', 'store_product' => 'string', 'phone_code_hash' => 'string', 'support_email_address' => 'string', 'support_email_subject' => 'string'];
```  
