---
title: "messageActionPaidMessagesRefunded"
description: "Sent from peer A to B, indicates that A refunded all stars B previously paid to send messages to A, see here » for more info on paid messages."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageActionPaidMessagesRefunded  
[Back to constructors index](/API_docs/constructors/index.html)



Sent from peer A to B, indicates that A refunded all [stars](https://core.telegram.org/api/stars) B previously paid to send messages to A, see [here »](https://core.telegram.org/api/paid-messages) for more info on paid messages.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|count|[int](/API_docs/types/int.html) | Yes|Number of paid messages affected by the refund.|
|stars|[long](/API_docs/types/long.html) | Yes|Number of refunded stars.|



### Type: [MessageAction](/API_docs/types/MessageAction.html)


### Example:

```
$messageActionPaidMessagesRefunded = ['_' => 'messageActionPaidMessagesRefunded', 'count' => int, 'stars' => long];
```  
