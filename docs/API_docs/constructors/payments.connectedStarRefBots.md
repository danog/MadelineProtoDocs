---
title: "payments.connectedStarRefBots"
description: "Active affiliations"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/payments_connectedStarRefBots.html
---
# Constructor: payments.connectedStarRefBots  
[Back to constructors index](/API_docs/constructors/index.html)



Active [affiliations](https://core.telegram.org/api/bots/referrals#becoming-an-affiliate)

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|count|[int](/API_docs/types/int.html) | Yes|Total number of active affiliations|
|connected\_bots|Array of [ConnectedBotStarRef](/API_docs/types/ConnectedBotStarRef.html) | Yes|The affiliations|
|users|Array of [User](/API_docs/types/User.html) | Yes|Peers mentioned in `connected_bots`|



### Type: [payments.ConnectedStarRefBots](/API_docs/types/payments.ConnectedStarRefBots.html)


### Example:

```
$payments_connectedStarRefBots = ['_' => 'payments.connectedStarRefBots', 'count' => int, 'connected_bots' => [ConnectedBotStarRef, ConnectedBotStarRef], 'users' => [User, User]];
```  
