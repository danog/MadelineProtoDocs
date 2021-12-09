---
title: shippingOption
description: Shipping option
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: shippingOption  
[Back to constructors index](index.md)



Shipping option

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[string](../types/string.md) | Yes|Option ID|
|title|[string](../types/string.md) | Yes|Title|
|prices|Array of [LabeledPrice](../types/LabeledPrice.md) | Yes|List of price portions|



### Type: [ShippingOption](../types/ShippingOption.md)


### Example:

```php
$shippingOption = ['_' => 'shippingOption', 'id' => 'string', 'title' => 'string', 'prices' => [LabeledPrice, LabeledPrice]];
```  


Or, if you're into Lua:

```lua
shippingOption={_='shippingOption', id='string', title='string', prices={LabeledPrice}}

```


