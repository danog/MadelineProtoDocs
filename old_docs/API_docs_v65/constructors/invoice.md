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
|test|[Bool](../types/Bool.md) | Optional|Test invoice|
|name\_requested|[Bool](../types/Bool.md) | Optional|Set this flag if you require the user's full name to complete the order|
|phone\_requested|[Bool](../types/Bool.md) | Optional|Set this flag if you require the user's phone number to complete the order|
|email\_requested|[Bool](../types/Bool.md) | Optional|Set this flag if you require the user's email address to complete the order|
|shipping\_address\_requested|[Bool](../types/Bool.md) | Optional|Set this flag if you require the user's shipping address to complete the order|
|flexible|[Bool](../types/Bool.md) | Optional|Set this flag if the final price depends on the shipping method|
|currency|[string](../types/string.md) | Yes|Three-letter ISO 4217 [currency](https://core.telegram.org/bots/payments#supported-currencies) code|
|prices|Array of [LabeledPrice](../types/LabeledPrice.md) | Yes|Prices|



### Type: [Invoice](../types/Invoice.md)


### Example:

```php
$invoice = ['_' => 'invoice', 'test' => Bool, 'name_requested' => Bool, 'phone_requested' => Bool, 'email_requested' => Bool, 'shipping_address_requested' => Bool, 'flexible' => Bool, 'currency' => 'string', 'prices' => [LabeledPrice, LabeledPrice]];
```  


Or, if you're into Lua:

```lua
invoice={_='invoice', test=Bool, name_requested=Bool, phone_requested=Bool, email_requested=Bool, shipping_address_requested=Bool, flexible=Bool, currency='string', prices={LabeledPrice}}

```


