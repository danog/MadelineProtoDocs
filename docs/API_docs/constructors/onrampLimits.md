---
title: "onrampLimits"
description: "onrampLimits attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: onrampLimits  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|base\_currency|[string](/API_docs/types/string.html) | Yes|
|base\_min\_amount|[string](/API_docs/types/string.html) | Yes|
|base\_max\_amount|[string](/API_docs/types/string.html) | Yes|
|crypto\_min\_amount|[string](/API_docs/types/string.html) | Yes|
|crypto\_max\_amount|[string](/API_docs/types/string.html) | Yes|
|payment\_method|[string](/API_docs/types/string.html) | Yes|



### Type: [OnrampLimits](/API_docs/types/OnrampLimits.html)


### Example:

```
$onrampLimits = ['_' => 'onrampLimits', 'base_currency' => 'string', 'base_min_amount' => 'string', 'base_max_amount' => 'string', 'crypto_min_amount' => 'string', 'crypto_max_amount' => 'string', 'payment_method' => 'string'];
```  
