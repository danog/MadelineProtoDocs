---
title: "inputBotInlineMessageMediaInvoice"
description: "An invoice"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputBotInlineMessageMediaInvoice  
[Back to constructors index](/API_docs/constructors/index.html)



An invoice

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|title|[string](/API_docs/types/string.html) | Yes|Product name, 1-32 characters|
|description|[string](/API_docs/types/string.html) | Yes|Product description, 1-255 characters|
|photo|[InputWebDocument](/API_docs/types/InputWebDocument.html) | Optional|Invoice photo|
|invoice|[Invoice](/API_docs/types/Invoice.html) | Yes|The invoice|
|payload|[bytes](/API_docs/types/bytes.html) | Yes|Bot-defined invoice payload, 1-128 bytes. This will not be displayed to the user, use for your internal processes.|
|provider|[string](/API_docs/types/string.html) | Yes|Payments provider token, obtained via [Botfather](https://t.me/botfather)|
|provider\_data|[DataJSON](/API_docs/types/DataJSON.html) | Yes|A JSON-serialized object for data about the invoice, which will be shared with the payment provider. A detailed description of the required fields should be provided by the payment provider.|
|reply\_markup|[ReplyMarkup](/API_docs/types/ReplyMarkup.html) | Optional|Inline keyboard|



### Type: [InputBotInlineMessage](/API_docs/types/InputBotInlineMessage.html)



## Usage of reply_markup

You can provide bot API reply_markup objects here.  


### Example:

```
$inputBotInlineMessageMediaInvoice = ['_' => 'inputBotInlineMessageMediaInvoice', 'title' => 'string', 'description' => 'string', 'photo' => InputWebDocument, 'invoice' => Invoice, 'payload' => 'bytes', 'provider' => 'string', 'provider_data' => DataJSON, 'reply_markup' => ReplyMarkup];
```  
