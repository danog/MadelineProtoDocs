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
|id|[string](../types/string.md) | Yes|ID|
|title|[string](../types/string.md) | Yes|Title|
|prices|Array of [LabeledPrice](../types/LabeledPrice.md) | Yes|Prices|



### Type: [ShippingOption](../types/ShippingOption.md)


### Example:

```php
$shippingOption = ['_' => 'shippingOption', 'id' => 'string', 'title' => 'string', 'prices' => [LabeledPrice, LabeledPrice]];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "shippingOption", "id": "string", "title": "string", "prices": [LabeledPrice]}
```


Or, if you're into Lua:

```lua
shippingOption={_='shippingOption', id='string', title='string', prices={LabeledPrice}}

```


