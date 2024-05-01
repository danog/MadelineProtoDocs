---
title: "paymentRequestedInfo"
description: "Order info provided by the user"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: paymentRequestedInfo  
[Back to constructors index](/API_docs/constructors/index.html)



Order info provided by the user

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|name|[string](/API_docs/types/string.html) | Optional|User's full name|
|phone|[string](/API_docs/types/string.html) | Optional|User's phone number|
|email|[string](/API_docs/types/string.html) | Optional|User's email address|
|shipping\_address|[PostAddress](/API_docs/types/PostAddress.html) | Optional|User's shipping address|



### Type: [PaymentRequestedInfo](/API_docs/types/PaymentRequestedInfo.html)


### Example:

```
$paymentRequestedInfo = ['_' => 'paymentRequestedInfo', 'name' => 'string', 'phone' => 'string', 'email' => 'string', 'shipping_address' => PostAddress];
```  
