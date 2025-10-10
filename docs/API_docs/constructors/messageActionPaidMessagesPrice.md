---
title: "messageActionPaidMessagesPrice"
description: "The price of paid messages » in this chat was changed."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageActionPaidMessagesPrice  
[Back to constructors index](/API_docs/constructors/index.html)



The price of [paid messages »](https://core.telegram.org/api/paid-messages) in this chat was changed.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|broadcast\_messages\_allowed|[Bool](/API_docs/types/Bool.html) | Optional|Can only be set for channels, if set indicates that [direct messages were enabled »](https://core.telegram.org/api/monoforum), otherwise indicates that direct messages were disabled; the price of paid messages is related to the price of direct messages (aka those sent to the associated [monoforum](https://core.telegram.org/api/monoforum)).|
|stars|[long](/API_docs/types/long.html) | Yes|The new price in [Telegram Stars](https://core.telegram.org/api/stars), can be `0` if messages are now free.|



### Type: [MessageAction](/API_docs/types/MessageAction.html)


### Example:

```
$messageActionPaidMessagesPrice = ['_' => 'messageActionPaidMessagesPrice', 'broadcast_messages_allowed' => Bool, 'stars' => long];
```  
