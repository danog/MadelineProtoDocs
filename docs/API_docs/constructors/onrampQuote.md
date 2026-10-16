---
title: "onrampQuote"
description: "onrampQuote attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: onrampQuote  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|base\_currency|[string](/API_docs/types/string.html) | Yes|
|base\_amount|[string](/API_docs/types/string.html) | Yes|
|crypto\_currency|[string](/API_docs/types/string.html) | Yes|
|crypto\_amount|[string](/API_docs/types/string.html) | Yes|
|crypto\_price|[string](/API_docs/types/string.html) | Yes|
|fee\_amount|[string](/API_docs/types/string.html) | Yes|
|extra\_fee\_amount|[string](/API_docs/types/string.html) | Yes|
|network\_fee\_amount|[string](/API_docs/types/string.html) | Yes|
|total\_amount|[string](/API_docs/types/string.html) | Yes|
|payment\_method|[string](/API_docs/types/string.html) | Yes|
|expires\_date|[int](/API_docs/types/int.html) | Yes|



### Type: [OnrampQuote](/API_docs/types/OnrampQuote.html)


### Example:

```
$onrampQuote = ['_' => 'onrampQuote', 'base_currency' => 'string', 'base_amount' => 'string', 'crypto_currency' => 'string', 'crypto_amount' => 'string', 'crypto_price' => 'string', 'fee_amount' => 'string', 'extra_fee_amount' => 'string', 'network_fee_amount' => 'string', 'total_amount' => 'string', 'payment_method' => 'string', 'expires_date' => int];
```  
