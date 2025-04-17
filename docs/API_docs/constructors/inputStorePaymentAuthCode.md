---
title: "inputStorePaymentAuthCode"
description: "inputStorePaymentAuthCode attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputStorePaymentAuthCode  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|restore|[Bool](/API_docs/types/Bool.html) | Optional|
|phone\_number|[string](/API_docs/types/string.html) | Yes|
|phone\_code\_hash|[string](/API_docs/types/string.html) | Yes|
|currency|[string](/API_docs/types/string.html) | Yes|
|amount|[long](/API_docs/types/long.html) | Yes|



### Type: [InputStorePaymentPurpose](/API_docs/types/InputStorePaymentPurpose.html)


### Example:

```
$inputStorePaymentAuthCode = ['_' => 'inputStorePaymentAuthCode', 'restore' => Bool, 'phone_number' => 'string', 'phone_code_hash' => 'string', 'currency' => 'string', 'amount' => long];
```  
