---
title: "botInlineMessageMediaInvoice"
description: "botInlineMessageMediaInvoice attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: botInlineMessageMediaInvoice  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|shipping\_address\_requested|[Bool](../types/Bool.md) | Optional|
|test|[Bool](../types/Bool.md) | Optional|
|title|[string](../types/string.md) | Yes|
|description|[string](../types/string.md) | Yes|
|photo|[WebDocument](../types/WebDocument.md) | Optional|
|currency|[string](../types/string.md) | Yes|
|total\_amount|[long](../types/long.md) | Yes|
|reply\_markup|[ReplyMarkup](../types/ReplyMarkup.md) | Optional|



### Type: [BotInlineMessage](../types/BotInlineMessage.md)


### Example:

```php
$botInlineMessageMediaInvoice = ['_' => 'botInlineMessageMediaInvoice', 'shipping_address_requested' => Bool, 'test' => Bool, 'title' => 'string', 'description' => 'string', 'photo' => WebDocument, 'currency' => 'string', 'total_amount' => long, 'reply_markup' => ReplyMarkup];
```  


Or, if you're into Lua:

```lua
botInlineMessageMediaInvoice={_='botInlineMessageMediaInvoice', shipping_address_requested=Bool, test=Bool, title='string', description='string', photo=WebDocument, currency='string', total_amount=long, reply_markup=ReplyMarkup}

```



## Usage of reply_markup

You can provide bot API reply_markup objects here.  


