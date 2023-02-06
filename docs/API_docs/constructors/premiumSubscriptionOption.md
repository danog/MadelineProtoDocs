---
title: "premiumSubscriptionOption"
description: "premiumSubscriptionOption attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: premiumSubscriptionOption  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|current|[Bool](/API_docs/types/Bool.html) | Optional|
|can\_purchase\_upgrade|[Bool](/API_docs/types/Bool.html) | Optional|
|transaction|[string](/API_docs/types/string.html) | Optional|
|months|[int](/API_docs/types/int.html) | Yes|
|currency|[string](/API_docs/types/string.html) | Yes|
|amount|[long](/API_docs/types/long.html) | Yes|
|bot\_url|[string](/API_docs/types/string.html) | Yes|
|store\_product|[string](/API_docs/types/string.html) | Optional|



### Type: [PremiumSubscriptionOption](/API_docs/types/PremiumSubscriptionOption.html)


### Example:

```
$premiumSubscriptionOption = ['_' => 'premiumSubscriptionOption', 'current' => Bool, 'can_purchase_upgrade' => Bool, 'transaction' => 'string', 'months' => int, 'currency' => 'string', 'amount' => long, 'bot_url' => 'string', 'store_product' => 'string'];
```  
