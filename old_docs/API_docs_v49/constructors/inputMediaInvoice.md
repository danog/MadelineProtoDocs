---
title: inputMediaInvoice
description: Generated invoice of a [bot payment](https://core.telegram.org/bots/payments)
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputMediaInvoice  
[Back to constructors index](index.md)



Generated invoice of a [bot payment](https://core.telegram.org/bots/payments)

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|title|[string](../types/string.md) | Yes|Product name, 1-32 characters|
|description|[string](../types/string.md) | Yes|Product description, 1-255 characters|
|photo|[InputWebDocument](../types/InputWebDocument.md) | Optional|URL of the product photo for the invoice. Can be a photo of the goods or a marketing image for a service. People like it better when they see what they are paying for.|
|invoice|[Invoice](../types/Invoice.md) | Yes|The actual invoice|
|payload|[bytes](../types/bytes.md) | Yes|Bot-defined invoice payload, 1-128 bytes. This will not be displayed to the user, use for your internal processes.|
|provider|[string](../types/string.md) | Yes|Payments provider token, obtained via [Botfather](https://t.me/botfather)|
|provider\_data|[DataJSON](../types/DataJSON.md) | Yes|JSON-encoded data about the invoice, which will be shared with the payment provider. A detailed description of required fields should be provided by the payment provider.|
|start\_param|[string](../types/string.md) | Optional|Start parameter|



### Type: [InputMedia](../types/InputMedia.md)


### Example:

```php
$inputMediaInvoice = ['_' => 'inputMediaInvoice', 'title' => 'string', 'description' => 'string', 'photo' => InputWebDocument, 'invoice' => Invoice, 'payload' => 'bytes', 'provider' => 'string', 'provider_data' => DataJSON, 'start_param' => 'string'];
```  


Or, if you're into Lua:

```lua
inputMediaInvoice={_='inputMediaInvoice', title='string', description='string', photo=InputWebDocument, invoice=Invoice, payload='bytes', provider='string', provider_data=DataJSON, start_param='string'}

```


