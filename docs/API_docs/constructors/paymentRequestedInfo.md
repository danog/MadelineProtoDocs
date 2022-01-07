---
title: "paymentRequestedInfo"
description: "Order info provided by the user"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: paymentRequestedInfo  
[Back to constructors index](/API_docs/constructors/index.md)



Order info provided by the user

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|name|[string](/API_docs/types/string.md) | Optional|User's full name|
|phone|[string](/API_docs/types/string.md) | Optional|User's phone number|
|email|[string](/API_docs/types/string.md) | Optional|User's email address|
|shipping\_address|[PostAddress](/API_docs/types/PostAddress.md) | Optional|User's shipping address|



### Type: [PaymentRequestedInfo](/API_docs/types/PaymentRequestedInfo.md)


### Example:

```php
$paymentRequestedInfo = ['_' => 'paymentRequestedInfo', 'name' => 'string', 'phone' => 'string', 'email' => 'string', 'shipping_address' => PostAddress];
```  
