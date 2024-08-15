---
title: "starsSubscription"
description: "starsSubscription attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: starsSubscription  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|canceled|[Bool](/API_docs/types/Bool.html) | Optional|
|can\_refulfill|[Bool](/API_docs/types/Bool.html) | Optional|
|missing\_balance|[Bool](/API_docs/types/Bool.html) | Optional|
|id|[string](/API_docs/types/string.html) | Yes|
|peer|[long](/API_docs/types/long.html) | Yes|
|until\_date|[int](/API_docs/types/int.html) | Yes|
|pricing|[StarsSubscriptionPricing](/API_docs/types/StarsSubscriptionPricing.html) | Yes|
|chat\_invite\_hash|[string](/API_docs/types/string.html) | Optional|



### Type: [StarsSubscription](/API_docs/types/StarsSubscription.html)


### Example:

```
$starsSubscription = ['_' => 'starsSubscription', 'canceled' => Bool, 'can_refulfill' => Bool, 'missing_balance' => Bool, 'id' => 'string', 'peer' => long, 'until_date' => int, 'pricing' => StarsSubscriptionPricing, 'chat_invite_hash' => 'string'];
```  
