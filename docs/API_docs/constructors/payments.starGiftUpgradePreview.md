---
title: "payments.starGiftUpgradePreview"
description: "A preview of the possible attributes (chosen randomly) a gift » can receive after upgrading it to a collectible gift », see here » for more info."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/payments_starGiftUpgradePreview.html
---
# Constructor: payments.starGiftUpgradePreview  
[Back to constructors index](/API_docs/constructors/index.html)



A preview of the possible attributes (chosen randomly) a [gift »](https://core.telegram.org/api/gifts) can receive after upgrading it to a [collectible gift »](https://core.telegram.org/api/gifts#collectible-gifts), see [here »](https://core.telegram.org/api/gifts#collectible-gifts) for more info.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|sample\_attributes|Array of [StarGiftAttribute](/API_docs/types/StarGiftAttribute.html) | Yes|Possible gift attributes|
|prices|Array of [StarGiftUpgradePrice](/API_docs/types/StarGiftUpgradePrice.html) | Yes|
|next\_prices|Array of [StarGiftUpgradePrice](/API_docs/types/StarGiftUpgradePrice.html) | Yes|



### Type: [payments.StarGiftUpgradePreview](/API_docs/types/payments.StarGiftUpgradePreview.html)


### Example:

```
$payments_starGiftUpgradePreview = ['_' => 'payments.starGiftUpgradePreview', 'sample_attributes' => [StarGiftAttribute, StarGiftAttribute], 'prices' => [StarGiftUpgradePrice, StarGiftUpgradePrice], 'next_prices' => [StarGiftUpgradePrice, StarGiftUpgradePrice]];
```  
