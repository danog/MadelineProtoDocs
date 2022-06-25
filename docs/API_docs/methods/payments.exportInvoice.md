---
title: "payments.exportInvoice"
description: "payments.exportInvoice parameters, return type and example"
grand_parent: "Telegram RPC API"
parent: "Methods"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/methods/payments_exportInvoice.html
---
# Method: payments.exportInvoice
[Back to methods index](index.html)



### Parameters:

| Name     |    Type       | Required |
|----------|---------------|----------|
|invoice\_media|[MessageMedia, Update, Message or InputMedia](/API_docs/types/InputMedia.html) | Optional|


### Return type: [payments.ExportedInvoice](/API_docs/types/payments.ExportedInvoice.html)

### Can bots use this method: **YES**


### MadelineProto Example ([now async for huge speed and parallelism!](https://docs.madelineproto.xyz/docs/ASYNC.html)):


```php
if (!file_exists('madeline.php')) {
    copy('https://phar.madelineproto.xyz/madeline.php', 'madeline.php');
}
include 'madeline.php';

$MadelineProto = new \danog\MadelineProto\API('session.madeline');
$MadelineProto->start();

// PHP 8+ syntax, use an array on PHP 7.
$payments_ExportedInvoice = $MadelineProto->payments->exportInvoice(invoice_media: InputMedia, );
```

