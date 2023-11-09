---
title: "premium.boostsStatus"
description: "premium.boostsStatus attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/premium_boostsStatus.html
---
# Constructor: premium.boostsStatus  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|my\_boost|[Bool](/API_docs/types/Bool.html) | Optional|
|level|[int](/API_docs/types/int.html) | Yes|
|current\_level\_boosts|[int](/API_docs/types/int.html) | Yes|
|boosts|[int](/API_docs/types/int.html) | Yes|
|gift\_boosts|[int](/API_docs/types/int.html) | Optional|
|next\_level\_boosts|[int](/API_docs/types/int.html) | Optional|
|premium\_audience|[StatsPercentValue](/API_docs/types/StatsPercentValue.html) | Optional|
|boost\_url|[string](/API_docs/types/string.html) | Yes|
|prepaid\_giveaways|Array of [PrepaidGiveaway](/API_docs/types/PrepaidGiveaway.html) | Optional|
|my\_boost\_slots|Array of [int](/API_docs/types/int.html) | Optional|



### Type: [premium.BoostsStatus](/API_docs/types/premium.BoostsStatus.html)


### Example:

```
$premium_boostsStatus = ['_' => 'premium.boostsStatus', 'my_boost' => Bool, 'level' => int, 'current_level_boosts' => int, 'boosts' => int, 'gift_boosts' => int, 'next_level_boosts' => int, 'premium_audience' => StatsPercentValue, 'boost_url' => 'string', 'prepaid_giveaways' => [PrepaidGiveaway, PrepaidGiveaway], 'my_boost_slots' => [int, int]];
```  
