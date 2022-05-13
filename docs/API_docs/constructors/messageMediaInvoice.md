---
title: "messageMediaInvoice"
description: "Invoice"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageMediaInvoice  
[Back to constructors index](/API_docs/constructors/index.html)



Invoice

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|shipping\_address\_requested|[Bool](/API_docs/types/Bool.html) | Optional|Whether the shipping address was requested|
|test|[Bool](/API_docs/types/Bool.html) | Optional|Whether this is an example invoice|
|title|[string](/API_docs/types/string.html) | Yes|Product name, 1-32 characters|
|description|[string](/API_docs/types/string.html) | Yes|Product description, 1-255 characters|
|photo|[WebDocument](/API_docs/types/WebDocument.html) | Optional|URL of the product photo for the invoice. Can be a photo of the goods or a marketing image for a service. People like it better when they see what they are paying for.|
|receipt\_msg\_id|[int](/API_docs/types/int.html) | Optional|Message ID of receipt: if set, clients should change the text of the first [keyboardButtonBuy](../constructors/keyboardButtonBuy.html) button always attached to the [message](../constructors/message.html) to a localized version of the word `Receipt`|
|currency|[string](/API_docs/types/string.html) | Yes|Three-letter ISO 4217 [currency](https://core.telegram.org/bots/payments#supported-currencies) code|
|total\_amount|[long](/API_docs/types/long.html) | Yes|Total price in the smallest units of the currency (integer, not float/double). For example, for a price of `US$ 1.45` pass `amount = 145`. See the exp parameter in [currencies.json](https://core.telegram.org/bots/payments/currencies.json), it shows the number of digits past the decimal point for each currency (2 for the majority of currencies).|
|start\_param|[string](/API_docs/types/string.html) | Yes|Unique bot deep-linking parameter that can be used to generate this invoice|



### Type: [MessageMedia](/API_docs/types/MessageMedia.html)


### Example:

```
$messageMediaInvoice = ['_' => 'messageMediaInvoice', 'shipping_address_requested' => Bool, 'test' => Bool, 'title' => 'string', 'description' => 'string', 'photo' => WebDocument, 'receipt_msg_id' => int, 'currency' => 'string', 'total_amount' => long, 'start_param' => 'string'];
```  
