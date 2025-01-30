---
title: "starRefProgram"
description: "Indo about an affiliate program offered by a bot"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: starRefProgram  
[Back to constructors index](/API_docs/constructors/index.html)



Indo about an [affiliate program offered by a bot](https://core.telegram.org/api/bots/referrals)

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|bot\_id|[long](/API_docs/types/long.html) | Yes|ID of the bot that offers the program|
|commission\_permille|[int](/API_docs/types/int.html) | Yes|An affiliate gets a commission of [starRefProgram](../constructors/starRefProgram.html).`commission_permille`‰ [Telegram Stars](https://core.telegram.org/api/stars) for every mini app transaction made by users they refer|
|duration\_months|[int](/API_docs/types/int.html) | Optional|An affiliate gets a commission for every mini app transaction made by users they refer, for `duration_months` months after a referral link is imported, starting the bot for the first time|
|end\_date|[int](/API_docs/types/int.html) | Optional|Point in time (Unix timestamp) when the affiliate program will be closed (optional, if not set the affiliate program isn't scheduled to be closed)|
|daily\_revenue\_per\_user|[StarsAmount](/API_docs/types/StarsAmount.html) | Optional|The amount of daily revenue per user in Telegram Stars of the bot that created the affiliate program. <br>To obtain the approximated revenue per referred user, multiply this value by `commission_permille` and divide by `1000`.|



### Type: [StarRefProgram](/API_docs/types/StarRefProgram.html)


### Example:

```
$starRefProgram = ['_' => 'starRefProgram', 'bot_id' => long, 'commission_permille' => int, 'duration_months' => int, 'end_date' => int, 'daily_revenue_per_user' => StarsAmount];
```  
