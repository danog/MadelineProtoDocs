---
title: "inputBotInlineMessageMediaInvoice"
description: "inputBotInlineMessageMediaInvoice attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputBotInlineMessageMediaInvoice  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|title|[string](/API_docs/types/string.html) | Yes|
|description|[string](/API_docs/types/string.html) | Yes|
|photo|[InputWebDocument](/API_docs/types/InputWebDocument.html) | Optional|
|invoice|[Invoice](/API_docs/types/Invoice.html) | Yes|
|payload|[bytes](/API_docs/types/bytes.html) | Yes|
|provider|[string](/API_docs/types/string.html) | Yes|
|provider\_data|[DataJSON](/API_docs/types/DataJSON.html) | Yes|
|reply\_markup|[ReplyMarkup](/API_docs/types/ReplyMarkup.html) | Optional|



### Type: [InputBotInlineMessage](/API_docs/types/InputBotInlineMessage.html)


### Example:

```php
$inputBotInlineMessageMediaInvoice = ['_' => 'inputBotInlineMessageMediaInvoice', 'title' => 'string', 'description' => 'string', 'photo' => InputWebDocument, 'invoice' => Invoice, 'payload' => 'bytes', 'provider' => 'string', 'provider_data' => DataJSON, 'reply_markup' => ReplyMarkup];
```  

## Usage of reply_markup

You can provide bot API reply_markup objects here.  


