---
title: "fragment.collectibleInfo"
description: "fragment.collectibleInfo attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/fragment_collectibleInfo.html
---
# Constructor: fragment.collectibleInfo  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|purchase\_date|[int](/API_docs/types/int.html) | Yes|
|currency|[string](/API_docs/types/string.html) | Yes|
|amount|[long](/API_docs/types/long.html) | Yes|
|crypto\_currency|[string](/API_docs/types/string.html) | Yes|
|crypto\_amount|[long](/API_docs/types/long.html) | Yes|
|url|[string](/API_docs/types/string.html) | Yes|



### Type: [fragment.CollectibleInfo](/API_docs/types/fragment.CollectibleInfo.html)


### Example:

```
$fragment_collectibleInfo = ['_' => 'fragment.collectibleInfo', 'purchase_date' => int, 'currency' => 'string', 'amount' => long, 'crypto_currency' => 'string', 'crypto_amount' => long, 'url' => 'string'];
```  
