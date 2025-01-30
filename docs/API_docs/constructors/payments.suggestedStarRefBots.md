---
title: "payments.suggestedStarRefBots"
description: "A list of suggested mini apps with available affiliate programs"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/payments_suggestedStarRefBots.html
---
# Constructor: payments.suggestedStarRefBots  
[Back to constructors index](/API_docs/constructors/index.html)



A list of suggested [mini apps](https://core.telegram.org/api/bots/webapps) with available [affiliate programs](https://core.telegram.org/api/bots/referrals)

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|count|[int](/API_docs/types/int.html) | Yes|Total number of results (for pagination)|
|suggested\_bots|Array of [StarRefProgram](/API_docs/types/StarRefProgram.html) | Yes|Suggested affiliate programs (full or partial list to be fetched using pagination)|
|users|Array of [User](/API_docs/types/User.html) | Yes|Peers mentioned in `suggested_bots`|
|next\_offset|[string](/API_docs/types/string.html) | Optional|Next offset for [pagination](https://core.telegram.org/api/offsets)|



### Type: [payments.SuggestedStarRefBots](/API_docs/types/payments.SuggestedStarRefBots.html)


### Example:

```
$payments_suggestedStarRefBots = ['_' => 'payments.suggestedStarRefBots', 'count' => int, 'suggested_bots' => [StarRefProgram, StarRefProgram], 'users' => [User, User], 'next_offset' => 'string'];
```  
