---
title: "payments.bankCardData"
description: "Credit card info, provided by the card's bank(s)"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/payments_bankCardData.html
---
# Constructor: payments.bankCardData  
[Back to constructors index](index.md)



Credit card info, provided by the card's bank(s)

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|title|[string](../types/string.md) | Yes|Credit card title|
|open\_urls|Array of [BankCardOpenUrl](../types/BankCardOpenUrl.md) | Yes|Info URL(s) provided by the card's bank(s)|



### Type: [payments.BankCardData](../types/payments.BankCardData.md)


### Example:

```php
$payments_bankCardData = ['_' => 'payments.bankCardData', 'title' => 'string', 'open_urls' => [BankCardOpenUrl, BankCardOpenUrl]];
```  


Or, if you're into Lua:

```lua
payments_bankCardData={_='payments.bankCardData', title='string', open_urls={BankCardOpenUrl}}

```


