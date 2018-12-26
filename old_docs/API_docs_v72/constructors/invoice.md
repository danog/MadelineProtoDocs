---
title: invoice
description: Invoice
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: invoice  
[Back to constructors index](index.md)



Invoice

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|test|[Bool](../types/Bool.md) | Optional|Test?|
|name\_requested|[Bool](../types/Bool.md) | Optional|Name requested?|
|phone\_requested|[Bool](../types/Bool.md) | Optional|Phone requested?|
|email\_requested|[Bool](../types/Bool.md) | Optional|Email requested?|
|shipping\_address\_requested|[Bool](../types/Bool.md) | Optional|Shipping address requested?|
|flexible|[Bool](../types/Bool.md) | Optional|Flexible?|
|currency|[string](../types/string.md) | Yes|Currency|
|prices|Array of [LabeledPrice](../types/LabeledPrice.md) | Yes|Prices|



### Type: [Invoice](../types/Invoice.md)


### Example:

```php
$invoice = ['_' => 'invoice', 'test' => Bool, 'name_requested' => Bool, 'phone_requested' => Bool, 'email_requested' => Bool, 'shipping_address_requested' => Bool, 'flexible' => Bool, 'currency' => 'string', 'prices' => [LabeledPrice, LabeledPrice]];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "invoice", "test": Bool, "name_requested": Bool, "phone_requested": Bool, "email_requested": Bool, "shipping_address_requested": Bool, "flexible": Bool, "currency": "string", "prices": [LabeledPrice]}
```


Or, if you're into Lua:

```lua
invoice={_='invoice', test=Bool, name_requested=Bool, phone_requested=Bool, email_requested=Bool, shipping_address_requested=Bool, flexible=Bool, currency='string', prices={LabeledPrice}}

```


