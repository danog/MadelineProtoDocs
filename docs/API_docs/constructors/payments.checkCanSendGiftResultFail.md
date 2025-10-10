---
title: "payments.checkCanSendGiftResultFail"
description: "The specified gift cannot be sent yet for the specified reason."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/payments_checkCanSendGiftResultFail.html
---
# Constructor: payments.checkCanSendGiftResultFail  
[Back to constructors index](/API_docs/constructors/index.html)



The specified gift cannot be sent yet for the specified reason.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|reason|[TextWithEntities](/API_docs/types/TextWithEntities.html) | Yes|The reason why it can't be sent yet.|



### Type: [payments.CheckCanSendGiftResult](/API_docs/types/payments.CheckCanSendGiftResult.html)


### Example:

```
$payments_checkCanSendGiftResultFail = ['_' => 'payments.checkCanSendGiftResultFail', 'reason' => TextWithEntities];
```  
