---
title: "sendAsPeer"
description: "Indicates a peer that can be used to send messages"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: sendAsPeer  
[Back to constructors index](/API_docs/constructors/index.html)



Indicates a peer that can be used to send messages

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|premium\_required|[Bool](/API_docs/types/Bool.html) | Optional|Whether a Telegram Premium account is required to send messages as this peer|
|peer|[Peer](/API_docs/types/Peer.html) | Yes|Peer|



### Type: [SendAsPeer](/API_docs/types/SendAsPeer.html)


### Example:

```
$sendAsPeer = ['_' => 'sendAsPeer', 'premium_required' => Bool, 'peer' => Peer];
```  
