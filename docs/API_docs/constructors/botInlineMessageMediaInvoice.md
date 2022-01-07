---
title: "botInlineMessageMediaInvoice"
description: "botInlineMessageMediaInvoice attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: botInlineMessageMediaInvoice  
[Back to constructors index](/API_docs/constructors/index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|shipping\_address\_requested|[Bool](/API_docs/types/Bool.md) | Optional|
|test|[Bool](/API_docs/types/Bool.md) | Optional|
|title|[string](/API_docs/types/string.md) | Yes|
|description|[string](/API_docs/types/string.md) | Yes|
|photo|[WebDocument](/API_docs/types/WebDocument.md) | Optional|
|currency|[string](/API_docs/types/string.md) | Yes|
|total\_amount|[long](/API_docs/types/long.md) | Yes|
|reply\_markup|[ReplyMarkup](/API_docs/types/ReplyMarkup.md) | Optional|



### Type: [BotInlineMessage](/API_docs/types/BotInlineMessage.md)


### Example:

```php
$botInlineMessageMediaInvoice = ['_' => 'botInlineMessageMediaInvoice', 'shipping_address_requested' => Bool, 'test' => Bool, 'title' => 'string', 'description' => 'string', 'photo' => WebDocument, 'currency' => 'string', 'total_amount' => long, 'reply_markup' => ReplyMarkup];
```  

## Usage of reply_markup

You can provide bot API reply_markup objects here.  


