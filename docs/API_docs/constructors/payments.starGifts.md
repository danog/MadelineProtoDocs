---
title: "payments.starGifts"
description: "payments.starGifts attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/payments_starGifts.html
---
# Constructor: payments.starGifts  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|hash|[int](/API_docs/types/int.html) | Yes|
|gifts|Array of [StarGift](/API_docs/types/StarGift.html) | Yes|



### Type: [payments.StarGifts](/API_docs/types/payments.StarGifts.html)


### Example:

```
$payments_starGifts = ['_' => 'payments.starGifts', 'hash' => int, 'gifts' => [StarGift, StarGift]];
```  
