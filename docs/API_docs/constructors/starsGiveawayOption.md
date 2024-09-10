---
title: "starsGiveawayOption"
description: "starsGiveawayOption attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: starsGiveawayOption  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|extended|[Bool](/API_docs/types/Bool.html) | Optional|
|default|[Bool](/API_docs/types/Bool.html) | Optional|
|stars|[long](/API_docs/types/long.html) | Yes|
|yearly\_boosts|[int](/API_docs/types/int.html) | Yes|
|store\_product|[string](/API_docs/types/string.html) | Optional|
|currency|[string](/API_docs/types/string.html) | Yes|
|amount|[long](/API_docs/types/long.html) | Yes|
|winners|Array of [StarsGiveawayWinnersOption](/API_docs/types/StarsGiveawayWinnersOption.html) | Yes|



### Type: [StarsGiveawayOption](/API_docs/types/StarsGiveawayOption.html)


### Example:

```
$starsGiveawayOption = ['_' => 'starsGiveawayOption', 'extended' => Bool, 'default' => Bool, 'stars' => long, 'yearly_boosts' => int, 'store_product' => 'string', 'currency' => 'string', 'amount' => long, 'winners' => [StarsGiveawayWinnersOption, StarsGiveawayWinnersOption]];
```  
