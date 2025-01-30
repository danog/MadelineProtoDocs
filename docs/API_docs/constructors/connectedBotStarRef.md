---
title: "connectedBotStarRef"
description: "Info about an active affiliate program we have with a Mini App"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: connectedBotStarRef  
[Back to constructors index](/API_docs/constructors/index.html)



Info about an [active affiliate program we have with a Mini App](https://core.telegram.org/api/bots/referrals#becoming-an-affiliate)

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|revoked|[Bool](/API_docs/types/Bool.html) | Optional|If set, this affiliation was revoked by the affiliate using [payments.editConnectedStarRefBot](../methods/payments.editConnectedStarRefBot.html), or by the affiliation program owner using [bots.updateStarRefProgram](../methods/bots.updateStarRefProgram.html)|
|url|[string](/API_docs/types/string.html) | Yes|[Referral link](https://core.telegram.org/api/links#referral-links) to be shared|
|date|[int](/API_docs/types/int.html) | Yes|When did we affiliate with `bot_id`|
|bot\_id|[long](/API_docs/types/long.html) | Yes|ID of the mini app that created the affiliate program|
|commission\_permille|[int](/API_docs/types/int.html) | Yes|The number of Telegram Stars received by the affiliate for each 1000 Telegram Stars received by `bot_id`|
|duration\_months|[int](/API_docs/types/int.html) | Optional|Number of months the program will be active; if not set, there is no expiration date.|
|participants|[long](/API_docs/types/long.html) | Yes|The number of users that used the affiliate program|
|revenue|[long](/API_docs/types/long.html) | Yes|The number of Telegram Stars that were earned by the affiliate program|



### Type: [ConnectedBotStarRef](/API_docs/types/ConnectedBotStarRef.html)


### Example:

```
$connectedBotStarRef = ['_' => 'connectedBotStarRef', 'revoked' => Bool, 'url' => 'string', 'date' => int, 'bot_id' => long, 'commission_permille' => int, 'duration_months' => int, 'participants' => long, 'revenue' => long];
```  
