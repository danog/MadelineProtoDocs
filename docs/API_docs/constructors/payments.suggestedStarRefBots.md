---
title: "payments.suggestedStarRefBots"
description: "payments.suggestedStarRefBots attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/payments_suggestedStarRefBots.html
---
# Constructor: payments.suggestedStarRefBots  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|count|[int](/API_docs/types/int.html) | Yes|
|suggested\_bots|Array of [StarRefProgram](/API_docs/types/StarRefProgram.html) | Yes|
|users|Array of [User](/API_docs/types/User.html) | Yes|
|next\_offset|[string](/API_docs/types/string.html) | Optional|



### Type: [payments.SuggestedStarRefBots](/API_docs/types/payments.SuggestedStarRefBots.html)


### Example:

```
$payments_suggestedStarRefBots = ['_' => 'payments.suggestedStarRefBots', 'count' => int, 'suggested_bots' => [StarRefProgram, StarRefProgram], 'users' => [User, User], 'next_offset' => 'string'];
```  
