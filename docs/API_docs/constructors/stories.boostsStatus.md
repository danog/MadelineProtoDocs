---
title: "stories.boostsStatus"
description: "stories.boostsStatus attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/stories_boostsStatus.html
---
# Constructor: stories.boostsStatus  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|my\_boost|[Bool](/API_docs/types/Bool.html) | Optional|
|level|[int](/API_docs/types/int.html) | Yes|
|current\_level\_boosts|[int](/API_docs/types/int.html) | Yes|
|boosts|[int](/API_docs/types/int.html) | Yes|
|next\_level\_boosts|[int](/API_docs/types/int.html) | Optional|
|premium\_audience|[StatsPercentValue](/API_docs/types/StatsPercentValue.html) | Optional|



### Type: [stories.BoostsStatus](/API_docs/types/stories.BoostsStatus.html)


### Example:

```
$stories_boostsStatus = ['_' => 'stories.boostsStatus', 'my_boost' => Bool, 'level' => int, 'current_level_boosts' => int, 'boosts' => int, 'next_level_boosts' => int, 'premium_audience' => StatsPercentValue];
```  
