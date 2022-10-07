---
title: "paymentFormMethod"
description: "Represents an additional payment method"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: paymentFormMethod  
[Back to constructors index](/API_docs/constructors/index.html)



Represents an additional payment method

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|url|[string](/API_docs/types/string.html) | Yes|URL to open in a webview to process the payment|
|title|[string](/API_docs/types/string.html) | Yes|Payment method description|



### Type: [PaymentFormMethod](/API_docs/types/PaymentFormMethod.html)


### Example:

```
$paymentFormMethod = ['_' => 'paymentFormMethod', 'url' => 'string', 'title' => 'string'];
```  
