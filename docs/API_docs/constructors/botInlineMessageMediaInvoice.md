---
title: "botInlineMessageMediaInvoice"
description: "botInlineMessageMediaInvoice attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: botInlineMessageMediaInvoice  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|shipping\_address\_requested|[Bool](/API_docs/types/Bool.html) | Optional|
|test|[Bool](/API_docs/types/Bool.html) | Optional|
|title|[string](/API_docs/types/string.html) | Yes|
|description|[string](/API_docs/types/string.html) | Yes|
|photo|[WebDocument](/API_docs/types/WebDocument.html) | Optional|
|currency|[string](/API_docs/types/string.html) | Yes|
|total\_amount|[long](/API_docs/types/long.html) | Yes|
|reply\_markup|[ReplyMarkup](/API_docs/types/ReplyMarkup.html) | Optional|



### Type: [BotInlineMessage](/API_docs/types/BotInlineMessage.html)


### Example:

```php
$botInlineMessageMediaInvoice = ['_' => 'botInlineMessageMediaInvoice', 'shipping_address_requested' => Bool, 'test' => Bool, 'title' => 'string', 'description' => 'string', 'photo' => WebDocument, 'currency' => 'string', 'total_amount' => long, 'reply_markup' => ReplyMarkup];
```  

## Usage of reply_markup

You can provide bot API reply_markup objects here.  


