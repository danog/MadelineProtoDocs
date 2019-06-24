---
title: messageMediaInvoice
description: Message media invoice
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageMediaInvoice  
[Back to constructors index](index.md)



Message media invoice

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|shipping\_address\_requested|[Bool](../types/Bool.md) | Optional|Shipping address requested?|
|test|[Bool](../types/Bool.md) | Optional|Test?|
|title|[string](../types/string.md) | Yes|Title|
|description|[string](../types/string.md) | Yes|Description|
|photo|[WebDocument](../types/WebDocument.md) | Optional|Photo|
|receipt\_msg\_id|[int](../types/int.md) | Optional|Receipt msg ID|
|currency|[string](../types/string.md) | Yes|Currency|
|total\_amount|[long](../types/long.md) | Yes|Total amount|
|start\_param|[string](../types/string.md) | Yes|Start param|



### Type: [MessageMedia](../types/MessageMedia.md)


### Example:

```php
$messageMediaInvoice = ['_' => 'messageMediaInvoice', 'shipping_address_requested' => Bool, 'test' => Bool, 'title' => 'string', 'description' => 'string', 'photo' => WebDocument, 'receipt_msg_id' => int, 'currency' => 'string', 'total_amount' => long, 'start_param' => 'string'];
```  


Or, if you're into Lua:

```lua
messageMediaInvoice={_='messageMediaInvoice', shipping_address_requested=Bool, test=Bool, title='string', description='string', photo=WebDocument, receipt_msg_id=int, currency='string', total_amount=long, start_param='string'}

```


