---
title: payments.bankCardData
description: payments.bankCardData attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/payments_bankCardData.html
---
# Constructor: payments.bankCardData  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|title|[string](../types/string.md) | Yes|
|open\_urls|Array of [BankCardOpenUrl](../types/BankCardOpenUrl.md) | Yes|



### Type: [payments.BankCardData](../types/payments.BankCardData.md)


### Example:

```php
$payments.bankCardData = ['_' => 'payments.bankCardData', 'title' => 'string', 'open_urls' => [BankCardOpenUrl, BankCardOpenUrl]];
```  


Or, if you're into Lua:

```lua
payments.bankCardData={_='payments.bankCardData', title='string', open_urls={BankCardOpenUrl}}

```


