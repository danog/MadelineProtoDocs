---
title: "inputStorePaymentPremiumGiveaway"
description: "inputStorePaymentPremiumGiveaway attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputStorePaymentPremiumGiveaway  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|only\_new\_subscribers|[Bool](/API_docs/types/Bool.html) | Optional|
|boost\_peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Optional|
|additional\_peers|Array of [Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Optional|
|countries\_iso2|Array of [string](/API_docs/types/string.html) | Optional|
|until\_date|[int](/API_docs/types/int.html) | Yes|
|currency|[string](/API_docs/types/string.html) | Yes|
|amount|[long](/API_docs/types/long.html) | Yes|



### Type: [InputStorePaymentPurpose](/API_docs/types/InputStorePaymentPurpose.html)


### Example:

```
$inputStorePaymentPremiumGiveaway = ['_' => 'inputStorePaymentPremiumGiveaway', 'only_new_subscribers' => Bool, 'boost_peer' => InputPeer, 'additional_peers' => [InputPeer, InputPeer], 'countries_iso2' => ['string', 'string'], 'until_date' => int, 'currency' => 'string', 'amount' => long];
```  
