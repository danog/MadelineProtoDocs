---
title: "starsAmount"
description: "Describes a real (i.e. possibly decimal) amount of Telegram Stars."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: starsAmount  
[Back to constructors index](/API_docs/constructors/index.html)



Describes a real (i.e. possibly decimal) amount of [Telegram Stars](https://core.telegram.org/api/stars).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|amount|[long](/API_docs/types/long.html) | Yes|The integer amount of Telegram Stars.|
|nanos|[int](/API_docs/types/int.html) | Yes|The decimal amount of Telegram Stars, expressed as nanostars (i.e. 1 nanostar is equal to `1/1'000'000'000`th of a Telegram Star). <br>This field may also be negative (the allowed range is -999999999 to 999999999).|



### Type: [StarsAmount](/API_docs/types/StarsAmount.html)


### Example:

```
$starsAmount = ['_' => 'starsAmount', 'amount' => long, 'nanos' => int];
```  
