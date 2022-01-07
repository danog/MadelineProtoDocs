---
title: "inputBotInlineMessageMediaInvoice"
description: "inputBotInlineMessageMediaInvoice attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputBotInlineMessageMediaInvoice  
[Back to constructors index](/API_docs/constructors/index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|title|[string](/API_docs/types/string.md) | Yes|
|description|[string](/API_docs/types/string.md) | Yes|
|photo|[InputWebDocument](/API_docs/types/InputWebDocument.md) | Optional|
|invoice|[Invoice](/API_docs/types/Invoice.md) | Yes|
|payload|[bytes](/API_docs/types/bytes.md) | Yes|
|provider|[string](/API_docs/types/string.md) | Yes|
|provider\_data|[DataJSON](/API_docs/types/DataJSON.md) | Yes|
|reply\_markup|[ReplyMarkup](/API_docs/types/ReplyMarkup.md) | Optional|



### Type: [InputBotInlineMessage](/API_docs/types/InputBotInlineMessage.md)


### Example:

```php
$inputBotInlineMessageMediaInvoice = ['_' => 'inputBotInlineMessageMediaInvoice', 'title' => 'string', 'description' => 'string', 'photo' => InputWebDocument, 'invoice' => Invoice, 'payload' => 'bytes', 'provider' => 'string', 'provider_data' => DataJSON, 'reply_markup' => ReplyMarkup];
```  

## Usage of reply_markup

You can provide bot API reply_markup objects here.  


