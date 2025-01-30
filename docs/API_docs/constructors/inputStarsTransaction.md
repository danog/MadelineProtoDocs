---
title: "inputStarsTransaction"
description: "Used to fetch info about a Telegram Star transaction »."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputStarsTransaction  
[Back to constructors index](/API_docs/constructors/index.html)



Used to fetch info about a [Telegram Star transaction »](https://core.telegram.org/api/stars#balance-and-transaction-history).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|refund|[Bool](/API_docs/types/Bool.html) | Optional|If set, fetches info about the refund transaction for this transaction.|
|id|[string](/API_docs/types/string.html) | Yes|Transaction ID.|



### Type: [InputStarsTransaction](/API_docs/types/InputStarsTransaction.html)


### Example:

```
$inputStarsTransaction = ['_' => 'inputStarsTransaction', 'refund' => Bool, 'id' => 'string'];
```  
