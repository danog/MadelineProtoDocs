---
title: "premium.boostsStatus"
description: "Contains info about the current boost status of a peer."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/premium_boostsStatus.html
---
# Constructor: premium.boostsStatus  
[Back to constructors index](/API_docs/constructors/index.html)



Contains info about the current [boost status](https://core.telegram.org/api/boost) of a peer.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|my\_boost|[Bool](/API_docs/types/Bool.html) | Optional|Whether we're currently boosting this channel/supergroup, `my_boost_slots` will also be set.|
|level|[int](/API_docs/types/int.html) | Yes|The current boost level of the channel/supergroup.|
|current\_level\_boosts|[int](/API_docs/types/int.html) | Yes|The number of boosts acquired so far in the current level.|
|boosts|[int](/API_docs/types/int.html) | Yes|Total number of boosts acquired so far.|
|gift\_boosts|[int](/API_docs/types/int.html) | Optional|The number of boosts acquired from created Telegram Premium [gift codes](https://core.telegram.org/api/giveaways) and [giveaways](https://core.telegram.org/api/giveaways); only returned to channel/supergroup admins.|
|next\_level\_boosts|[int](/API_docs/types/int.html) | Optional|Total number of boosts needed to reach the next level; if absent, the next level isn't available.|
|premium\_audience|[StatsPercentValue](/API_docs/types/StatsPercentValue.html) | Optional|Only returned to channel/supergroup admins: contains the approximated number of Premium users subscribed to the channel/supergroup, related to the total number of subscribers.|
|boost\_url|[string](/API_docs/types/string.html) | Yes|[Boost deep link »](https://core.telegram.org/api/links#boost-links) that can be used to boost the chat.|
|prepaid\_giveaways|Array of [PrepaidGiveaway](/API_docs/types/PrepaidGiveaway.html) | Optional|A list of prepaid [giveaways](https://core.telegram.org/api/giveaways) available for the chat; only returned to channel/supergroup admins.|
|my\_boost\_slots|Array of [int](/API_docs/types/int.html) | Optional|Indicates which of our [boost slots](https://core.telegram.org/api/boost) we've assigned to this peer (populated if `my_boost` is set).|



### Type: [premium.BoostsStatus](/API_docs/types/premium.BoostsStatus.html)


### Example:

```
$premium_boostsStatus = ['_' => 'premium.boostsStatus', 'my_boost' => Bool, 'level' => int, 'current_level_boosts' => int, 'boosts' => int, 'gift_boosts' => int, 'next_level_boosts' => int, 'premium_audience' => StatsPercentValue, 'boost_url' => 'string', 'prepaid_giveaways' => [PrepaidGiveaway, PrepaidGiveaway], 'my_boost_slots' => [int, int]];
```  
