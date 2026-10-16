---
title: "payments.currencyRates"
description: "payments.currencyRates attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/payments_currencyRates.html
---
# Constructor: payments.currencyRates  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|rates|Array of [CurrencyRate](/API_docs/types/CurrencyRate.html) | Yes|



### Type: [payments.CurrencyRates](/API_docs/types/payments.CurrencyRates.html)


### Example:

```
$payments_currencyRates = ['_' => 'payments.currencyRates', 'rates' => [CurrencyRate, CurrencyRate]];
```  
