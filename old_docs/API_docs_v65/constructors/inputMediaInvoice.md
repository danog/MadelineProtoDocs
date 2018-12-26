---
title: inputMediaInvoice
description: Media invoice
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputMediaInvoice  
[Back to constructors index](index.md)



Media invoice

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|title|[string](../types/string.md) | Yes|Title|
|description|[string](../types/string.md) | Yes|Description|
|photo|[InputWebDocument](../types/InputWebDocument.md) | Optional|Photo|
|invoice|[Invoice](../types/Invoice.md) | Yes|Invoice|
|payload|[bytes](../types/bytes.md) | Yes|Payload|
|provider|[string](../types/string.md) | Yes|Provider|
|start\_param|[string](../types/string.md) | Yes|Start param|



### Type: [InputMedia](../types/InputMedia.md)


### Example:

```php
$inputMediaInvoice = ['_' => 'inputMediaInvoice', 'title' => 'string', 'description' => 'string', 'photo' => InputWebDocument, 'invoice' => Invoice, 'payload' => 'bytes', 'provider' => 'string', 'start_param' => 'string'];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "inputMediaInvoice", "title": "string", "description": "string", "photo": InputWebDocument, "invoice": Invoice, "payload": {"_": "bytes", "bytes":"base64 encoded bytes"}, "provider": "string", "start_param": "string"}
```


Or, if you're into Lua:

```lua
inputMediaInvoice={_='inputMediaInvoice', title='string', description='string', photo=InputWebDocument, invoice=Invoice, payload='bytes', provider='string', start_param='string'}

```


