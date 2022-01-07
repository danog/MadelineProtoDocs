---
title: "paymentCharge"
description: "Payment identifier"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: paymentCharge  
[Back to constructors index](/API_docs/constructors/index.md)



Payment identifier

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[string](/API_docs/types/string.md) | Yes|Telegram payment identifier|
|provider\_charge\_id|[string](/API_docs/types/string.md) | Yes|Provider payment identifier|



### Type: [PaymentCharge](/API_docs/types/PaymentCharge.md)


### Example:

```php
$paymentCharge = ['_' => 'paymentCharge', 'id' => 'string', 'provider_charge_id' => 'string'];
```  
