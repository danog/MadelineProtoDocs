---
title: "shippingOption"
description: "Shipping option"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: shippingOption  
[Back to constructors index](/API_docs/constructors/index.html)



Shipping option

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[string](/API_docs/types/string.html) | Yes|Option ID|
|title|[string](/API_docs/types/string.html) | Yes|Title|
|prices|Array of [LabeledPrice](/API_docs/types/LabeledPrice.html) | Yes|List of price portions|



### Type: [ShippingOption](/API_docs/types/ShippingOption.html)


### Example:

```
$shippingOption = ['_' => 'shippingOption', 'id' => 'string', 'title' => 'string', 'prices' => [LabeledPrice, LabeledPrice]];
```  
