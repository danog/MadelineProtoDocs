---
title: "shippingOption"
description: "Shipping option"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: shippingOption  
[Back to constructors index](/API_docs/constructors/index.md)



Shipping option

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[string](/API_docs/types/string.md) | Yes|Option ID|
|title|[string](/API_docs/types/string.md) | Yes|Title|
|prices|Array of [LabeledPrice](/API_docs/types/LabeledPrice.md) | Yes|List of price portions|



### Type: [ShippingOption](/API_docs/types/ShippingOption.md)


### Example:

```php
$shippingOption = ['_' => 'shippingOption', 'id' => 'string', 'title' => 'string', 'prices' => [LabeledPrice, LabeledPrice]];
```  
