---
title: "boost"
description: "Info about one or more boosts applied by a specific user."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: boost  
[Back to constructors index](/API_docs/constructors/index.html)



Info about one or more [boosts](https://core.telegram.org/api/boost) applied by a specific user.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|gift|[Bool](/API_docs/types/Bool.html) | Optional|Whether this boost was applied because the channel [directly gifted a subscription to the user](https://core.telegram.org/api/giveaways).|
|giveaway|[Bool](/API_docs/types/Bool.html) | Optional|Whether this boost was applied because the user was chosen in a [giveaway started by the channel](https://core.telegram.org/api/giveaways).|
|unclaimed|[Bool](/API_docs/types/Bool.html) | Optional|If set, the user hasn't yet invoked [payments.applyGiftCode](../methods/payments.applyGiftCode.html) to claim a subscription gifted [directly or in a giveaway by the channel](https://core.telegram.org/api/giveaways).|
|id|[string](/API_docs/types/string.html) | Yes|Unique ID for this set of boosts.|
|user\_id|[long](/API_docs/types/long.html) | Optional|ID of the user that applied the boost.|
|giveaway\_msg\_id|[int](/API_docs/types/int.html) | Optional|The message ID of the [giveaway](https://core.telegram.org/api/giveaways)|
|date|[int](/API_docs/types/int.html) | Yes|When was the boost applied|
|expires|[int](/API_docs/types/int.html) | Yes|When does the boost expire|
|used\_gift\_slug|[string](/API_docs/types/string.html) | Optional|The created Telegram Premium gift code, only set if either `gift` or `giveaway` are set AND it is either a gift code for the currently logged in user or if it was already claimed.|
|multiplier|[int](/API_docs/types/int.html) | Optional|If set, this boost counts as `multiplier` boosts, otherwise it counts as a single boost.|
|stars|[long](/API_docs/types/long.html) | Optional|



### Type: [Boost](/API_docs/types/Boost.html)


### Example:

```
$boost = ['_' => 'boost', 'gift' => Bool, 'giveaway' => Bool, 'unclaimed' => Bool, 'id' => 'string', 'user_id' => long, 'giveaway_msg_id' => int, 'date' => int, 'expires' => int, 'used_gift_slug' => 'string', 'multiplier' => int, 'stars' => long];
```  
