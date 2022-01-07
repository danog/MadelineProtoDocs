---
title: "labeledPrice"
description: "This object represents a portion of the price for goods or services."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: labeledPrice  
[Back to constructors index](/API_docs/constructors/index.md)



This object represents a portion of the price for goods or services.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|label|[string](/API_docs/types/string.md) | Yes|Portion label|
|amount|[long](/API_docs/types/long.md) | Yes|Price of the product in the smallest units of the currency (integer, not float/double). For example, for a price of `US$ 1.45` pass `amount = 145`. See the exp parameter in [currencies.json](https://core.telegram.org/bots/payments/currencies.json), it shows the number of digits past the decimal point for each currency (2 for the majority of currencies).|



### Type: [LabeledPrice](/API_docs/types/LabeledPrice.md)


### Example:

```php
$labeledPrice = ['_' => 'labeledPrice', 'label' => 'string', 'amount' => long];
```  
