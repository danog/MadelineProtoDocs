---
title: "inputStorePaymentPremiumSubscription"
description: "Info about a Telegram Premium purchase"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputStorePaymentPremiumSubscription  
[Back to constructors index](/API_docs/constructors/index.html)



Info about a Telegram Premium purchase

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|restore|[Bool](/API_docs/types/Bool.html) | Optional|Pass true if this is a restore of a Telegram Premium purchase; only for the App Store|



### Type: [InputStorePaymentPurpose](/API_docs/types/InputStorePaymentPurpose.html)


### Example:

```
$inputStorePaymentPremiumSubscription = ['_' => 'inputStorePaymentPremiumSubscription', 'restore' => Bool];
```  
