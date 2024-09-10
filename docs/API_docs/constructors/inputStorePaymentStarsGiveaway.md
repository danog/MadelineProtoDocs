---
title: "inputStorePaymentStarsGiveaway"
description: "inputStorePaymentStarsGiveaway attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputStorePaymentStarsGiveaway  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|only\_new\_subscribers|[Bool](/API_docs/types/Bool.html) | Optional|
|winners\_are\_visible|[Bool](/API_docs/types/Bool.html) | Optional|
|stars|[long](/API_docs/types/long.html) | Yes|
|boost\_peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Optional|
|additional\_peers|Array of [Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Optional|
|countries\_iso2|Array of [string](/API_docs/types/string.html) | Optional|
|prize\_description|[string](/API_docs/types/string.html) | Optional|
|until\_date|[int](/API_docs/types/int.html) | Yes|
|currency|[string](/API_docs/types/string.html) | Yes|
|amount|[long](/API_docs/types/long.html) | Yes|
|users|[int](/API_docs/types/int.html) | Yes|



### Type: [InputStorePaymentPurpose](/API_docs/types/InputStorePaymentPurpose.html)


### Example:

```
$inputStorePaymentStarsGiveaway = ['_' => 'inputStorePaymentStarsGiveaway', 'only_new_subscribers' => Bool, 'winners_are_visible' => Bool, 'stars' => long, 'boost_peer' => InputPeer, 'additional_peers' => [InputPeer, InputPeer], 'countries_iso2' => ['string', 'string'], 'prize_description' => 'string', 'until_date' => int, 'currency' => 'string', 'amount' => long, 'users' => int];
```  
