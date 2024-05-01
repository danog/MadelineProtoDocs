---
title: "botInlineMessageMediaInvoice"
description: "Send an invoice"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: botInlineMessageMediaInvoice  
[Back to constructors index](/API_docs/constructors/index.html)



Send an invoice

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|shipping\_address\_requested|[Bool](/API_docs/types/Bool.html) | Optional|Set this flag if you require the user's shipping address to complete the order|
|test|[Bool](/API_docs/types/Bool.html) | Optional|Test invoice|
|title|[string](/API_docs/types/string.html) | Yes|Product name, 1-32 characters|
|description|[string](/API_docs/types/string.html) | Yes|Product description, 1-255 characters|
|photo|[WebDocument](/API_docs/types/WebDocument.html) | Optional|Product photo|
|currency|[string](/API_docs/types/string.html) | Yes|Three-letter ISO 4217 [currency](https://core.telegram.org/bots/payments#supported-currencies) code|
|total\_amount|[long](/API_docs/types/long.html) | Yes|Total price in the smallest units of the currency (integer, not float/double). For example, for a price of `US$ 1.45` pass `amount = 145`. See the exp parameter in [currencies.json](https://core.telegram.org/bots/payments/currencies.json), it shows the number of digits past the decimal point for each currency (2 for the majority of currencies).|
|reply\_markup|[ReplyMarkup](/API_docs/types/ReplyMarkup.html) | Optional|Inline keyboard|



### Type: [BotInlineMessage](/API_docs/types/BotInlineMessage.html)



## Usage of reply_markup

You can provide bot API reply_markup objects here.  


### Example:

```
$botInlineMessageMediaInvoice = ['_' => 'botInlineMessageMediaInvoice', 'shipping_address_requested' => Bool, 'test' => Bool, 'title' => 'string', 'description' => 'string', 'photo' => WebDocument, 'currency' => 'string', 'total_amount' => long, 'reply_markup' => ReplyMarkup];
```  
