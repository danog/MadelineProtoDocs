---
title: "premiumGiftCodeOption"
description: "premiumGiftCodeOption attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: premiumGiftCodeOption  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|users|[int](/API_docs/types/int.html) | Yes|
|months|[int](/API_docs/types/int.html) | Yes|
|store\_product|[string](/API_docs/types/string.html) | Optional|
|store\_quantity|[int](/API_docs/types/int.html) | Optional|
|currency|[string](/API_docs/types/string.html) | Yes|
|amount|[long](/API_docs/types/long.html) | Yes|



### Type: [PremiumGiftCodeOption](/API_docs/types/PremiumGiftCodeOption.html)


### Example:

```
$premiumGiftCodeOption = ['_' => 'premiumGiftCodeOption', 'users' => int, 'months' => int, 'store_product' => 'string', 'store_quantity' => int, 'currency' => 'string', 'amount' => long];
```  
