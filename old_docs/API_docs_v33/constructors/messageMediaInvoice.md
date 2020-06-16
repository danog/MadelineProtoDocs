---
title: messageMediaInvoice
description: Invoice
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageMediaInvoice  
[Back to constructors index](index.md)



Invoice

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|shipping\_address\_requested|[Bool](../types/Bool.md) | Optional|Whether the shipping address was requested|
|test|[Bool](../types/Bool.md) | Optional|Whether this is an example invoice|
|title|[string](../types/string.md) | Yes|Product name, 1-32 characters|
|description|[string](../types/string.md) | Yes|Product description, 1-255 characters|
|photo|[WebDocument](../types/WebDocument.md) | Optional|URL of the product photo for the invoice. Can be a photo of the goods or a marketing image for a service. People like it better when they see what they are paying for.|
|receipt\_msg\_id|[int](../types/int.md) | Optional|Message ID of receipt: if set, clients should change the text of the first [keyboardButtonBuy](../constructors/keyboardButtonBuy.md) button always attached to the [message](../constructors/message.md) to a localized version of the word `Receipt`|
|currency|[string](../types/string.md) | Yes|Three-letter ISO 4217 [currency](https://core.telegram.org/bots/payments#supported-currencies) code|
|total\_amount|[long](../types/long.md) | Yes|Total price in the smallest units of the currency (integer, not float/double). For example, for a price of `US$ 1.45` pass `amount = 145`. See the exp parameter in [currencies.json](https://core.telegram.org/bots/payments/currencies.json), it shows the number of digits past the decimal point for each currency (2 for the majority of currencies).|
|start\_param|[string](../types/string.md) | Yes|Unique bot deep-linking parameter that can be used to generate this invoice|



### Type: [MessageMedia](../types/MessageMedia.md)


### Example:

```php
$messageMediaInvoice = ['_' => 'messageMediaInvoice', 'shipping_address_requested' => Bool, 'test' => Bool, 'title' => 'string', 'description' => 'string', 'photo' => WebDocument, 'receipt_msg_id' => int, 'currency' => 'string', 'total_amount' => long, 'start_param' => 'string'];
```  


Or, if you're into Lua:

```lua
messageMediaInvoice={_='messageMediaInvoice', shipping_address_requested=Bool, test=Bool, title='string', description='string', photo=WebDocument, receipt_msg_id=int, currency='string', total_amount=long, start_param='string'}

```


