---
title: "inputStorePaymentPremiumGiftCode"
description: "inputStorePaymentPremiumGiftCode attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputStorePaymentPremiumGiftCode  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|users|Array of [Username, chat ID, Update, Message or InputUser](/API_docs/types/InputUser.html) | Yes|
|boost\_peer|[Username, chat ID, Update, Message or InputPeer](/API_docs/types/InputPeer.html) | Optional|
|currency|[string](/API_docs/types/string.html) | Yes|
|amount|[long](/API_docs/types/long.html) | Yes|



### Type: [InputStorePaymentPurpose](/API_docs/types/InputStorePaymentPurpose.html)


### Example:

```
$inputStorePaymentPremiumGiftCode = ['_' => 'inputStorePaymentPremiumGiftCode', 'users' => [InputUser, InputUser], 'boost_peer' => InputPeer, 'currency' => 'string', 'amount' => long];
```  
