---
title: "starsGiveawayWinnersOption"
description: "Allowed options for the number of giveaway winners."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: starsGiveawayWinnersOption  
[Back to constructors index](/API_docs/constructors/index.html)



Allowed options for the number of giveaway winners.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|default|[Bool](/API_docs/types/Bool.html) | Optional|If set, this option must be pre-selected by default in the option list.|
|users|[int](/API_docs/types/int.html) | Yes|The number of users that will be randomly chosen as winners.|
|per\_user\_stars|[long](/API_docs/types/long.html) | Yes|The number of [Telegram Stars](https://core.telegram.org/api/stars) each winner will receive.|



### Type: [StarsGiveawayWinnersOption](/API_docs/types/StarsGiveawayWinnersOption.html)


### Example:

```
$starsGiveawayWinnersOption = ['_' => 'starsGiveawayWinnersOption', 'default' => Bool, 'users' => int, 'per_user_stars' => long];
```  
