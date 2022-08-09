---
title: "premiumGiftOption"
description: "premiumGiftOption attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: premiumGiftOption  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|months|[int](/API_docs/types/int.html) | Yes|
|currency|[string](/API_docs/types/string.html) | Yes|
|amount|[long](/API_docs/types/long.html) | Yes|
|bot\_url|[string](/API_docs/types/string.html) | Yes|
|store\_product|[string](/API_docs/types/string.html) | Optional|



### Type: [PremiumGiftOption](/API_docs/types/PremiumGiftOption.html)


### Example:

```
$premiumGiftOption = ['_' => 'premiumGiftOption', 'months' => int, 'currency' => 'string', 'amount' => long, 'bot_url' => 'string', 'store_product' => 'string'];
```  
