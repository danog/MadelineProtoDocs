---
title: "inputStorePaymentStarsGift"
description: "inputStorePaymentStarsGift attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputStorePaymentStarsGift  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|user\_id|[Username, chat ID, Update, Message or InputUser](/API_docs/types/InputUser.html) | Optional|
|stars|[long](/API_docs/types/long.html) | Yes|
|currency|[string](/API_docs/types/string.html) | Yes|
|amount|[long](/API_docs/types/long.html) | Yes|



### Type: [InputStorePaymentPurpose](/API_docs/types/InputStorePaymentPurpose.html)


### Example:

```
$inputStorePaymentStarsGift = ['_' => 'inputStorePaymentStarsGift', 'user_id' => InputUser, 'stars' => long, 'currency' => 'string', 'amount' => long];
```  
