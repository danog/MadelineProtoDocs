---
title: "payments.connectedStarRefBots"
description: "payments.connectedStarRefBots attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/payments_connectedStarRefBots.html
---
# Constructor: payments.connectedStarRefBots  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|count|[int](/API_docs/types/int.html) | Yes|
|connected\_bots|Array of [ConnectedBotStarRef](/API_docs/types/ConnectedBotStarRef.html) | Yes|
|users|Array of [User](/API_docs/types/User.html) | Yes|



### Type: [payments.ConnectedStarRefBots](/API_docs/types/payments.ConnectedStarRefBots.html)


### Example:

```
$payments_connectedStarRefBots = ['_' => 'payments.connectedStarRefBots', 'count' => int, 'connected_bots' => [ConnectedBotStarRef, ConnectedBotStarRef], 'users' => [User, User]];
```  
