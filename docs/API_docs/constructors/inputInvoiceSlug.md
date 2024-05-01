---
title: "inputInvoiceSlug"
description: "An invoice slug taken from an invoice deep link or from the premium_invoice_slug app config parameter »"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputInvoiceSlug  
[Back to constructors index](/API_docs/constructors/index.html)



An invoice slug taken from an [invoice deep link](https://core.telegram.org/api/links#invoice-links) or from the [`premium_invoice_slug` app config parameter »](https://core.telegram.org/api/config#premium-invoice-slug)

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|slug|[string](/API_docs/types/string.html) | Yes|The invoice slug|



### Type: [InputInvoice](/API_docs/types/InputInvoice.html)


### Example:

```
$inputInvoiceSlug = ['_' => 'inputInvoiceSlug', 'slug' => 'string'];
```  
