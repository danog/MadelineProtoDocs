---
title: "inputBotInlineMessageMediaInvoice"
description: "inputBotInlineMessageMediaInvoice attributes, type and example"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputBotInlineMessageMediaInvoice  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|title|[string](../types/string.md) | Yes|
|description|[string](../types/string.md) | Yes|
|photo|[InputWebDocument](../types/InputWebDocument.md) | Optional|
|invoice|[Invoice](../types/Invoice.md) | Yes|
|payload|[bytes](../types/bytes.md) | Yes|
|provider|[string](../types/string.md) | Yes|
|provider\_data|[DataJSON](../types/DataJSON.md) | Yes|
|reply\_markup|[ReplyMarkup](../types/ReplyMarkup.md) | Optional|



### Type: [InputBotInlineMessage](../types/InputBotInlineMessage.md)


### Example:

```php
$inputBotInlineMessageMediaInvoice = ['_' => 'inputBotInlineMessageMediaInvoice', 'title' => 'string', 'description' => 'string', 'photo' => InputWebDocument, 'invoice' => Invoice, 'payload' => 'bytes', 'provider' => 'string', 'provider_data' => DataJSON, 'reply_markup' => ReplyMarkup];
```  


Or, if you're into Lua:

```lua
inputBotInlineMessageMediaInvoice={_='inputBotInlineMessageMediaInvoice', title='string', description='string', photo=InputWebDocument, invoice=Invoice, payload='bytes', provider='string', provider_data=DataJSON, reply_markup=ReplyMarkup}

```



## Usage of reply_markup

You can provide bot API reply_markup objects here.  


