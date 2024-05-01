---
title: "payments.exportedInvoice"
description: "Exported invoice deep link"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/payments_exportedInvoice.html
---
# Constructor: payments.exportedInvoice  
[Back to constructors index](/API_docs/constructors/index.html)



Exported [invoice deep link](https://core.telegram.org/api/links#invoice-links)

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|url|[string](/API_docs/types/string.html) | Yes|Exported [invoice deep link](https://core.telegram.org/api/links#invoice-links)|



### Type: [payments.ExportedInvoice](/API_docs/types/payments.ExportedInvoice.html)


### Example:

```
$payments_exportedInvoice = ['_' => 'payments.exportedInvoice', 'url' => 'string'];
```  
