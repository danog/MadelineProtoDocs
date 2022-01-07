---
title: "invoice"
description: "Invoice"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: invoice  
[Back to constructors index](/API_docs/constructors/index.md)



Invoice

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|test|[Bool](/API_docs/types/Bool.md) | Optional|Test invoice|
|name\_requested|[Bool](/API_docs/types/Bool.md) | Optional|Set this flag if you require the user's full name to complete the order|
|phone\_requested|[Bool](/API_docs/types/Bool.md) | Optional|Set this flag if you require the user's phone number to complete the order|
|email\_requested|[Bool](/API_docs/types/Bool.md) | Optional|Set this flag if you require the user's email address to complete the order|
|shipping\_address\_requested|[Bool](/API_docs/types/Bool.md) | Optional|Set this flag if you require the user's shipping address to complete the order|
|flexible|[Bool](/API_docs/types/Bool.md) | Optional|Set this flag if the final price depends on the shipping method|
|phone\_to\_provider|[Bool](/API_docs/types/Bool.md) | Optional|Set this flag if user's phone number should be sent to provider|
|email\_to\_provider|[Bool](/API_docs/types/Bool.md) | Optional|Set this flag if user's email address should be sent to provider|
|currency|[string](/API_docs/types/string.md) | Yes|Three-letter ISO 4217 [currency](https://core.telegram.org/bots/payments#supported-currencies) code|
|prices|Array of [LabeledPrice](/API_docs/types/LabeledPrice.md) | Yes|Price breakdown, a list of components (e.g. product price, tax, discount, delivery cost, delivery tax, bonus, etc.)|
|max\_tip\_amount|[long](/API_docs/types/long.md) | Optional|
|suggested\_tip\_amounts|Array of [long](/API_docs/types/long.md) | Optional|



### Type: [Invoice](/API_docs/types/Invoice.md)


### Example:

```php
$invoice = ['_' => 'invoice', 'test' => Bool, 'name_requested' => Bool, 'phone_requested' => Bool, 'email_requested' => Bool, 'shipping_address_requested' => Bool, 'flexible' => Bool, 'phone_to_provider' => Bool, 'email_to_provider' => Bool, 'currency' => 'string', 'prices' => [LabeledPrice, LabeledPrice], 'max_tip_amount' => long, 'suggested_tip_amounts' => [long, long]];
```  
