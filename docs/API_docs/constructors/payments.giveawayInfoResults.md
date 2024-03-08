---
title: "payments.giveawayInfoResults"
description: "A giveaway has ended."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/payments_giveawayInfoResults.html
---
# Constructor: payments.giveawayInfoResults  
[Back to constructors index](/API_docs/constructors/index.html)



A [giveaway](https://core.telegram.org/api/giveaways) has ended.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|winner|[Bool](/API_docs/types/Bool.html) | Optional|Whether we're one of the winners of this giveaway.|
|refunded|[Bool](/API_docs/types/Bool.html) | Optional|Whether the giveaway was canceled and was fully refunded.|
|start\_date|[int](/API_docs/types/int.html) | Yes|Start date of the giveaway|
|gift\_code\_slug|[string](/API_docs/types/string.html) | Optional|If we're one of the winners of this giveaway, contains the [Premium gift code](https://core.telegram.org/api/links#premium-giftcode-links), see [here »](https://core.telegram.org/api/giveaways) for more info on the full giveaway flow.|
|finish\_date|[int](/API_docs/types/int.html) | Yes|End date of the giveaway. May be bigger than the end date specified in parameters of the giveaway.|
|winners\_count|[int](/API_docs/types/int.html) | Yes|Number of winners in the giveaway|
|activated\_count|[int](/API_docs/types/int.html) | Yes|Number of winners, which activated their [gift codes](https://core.telegram.org/api/links#premium-giftcode-links).|



### Type: [payments.GiveawayInfo](/API_docs/types/payments.GiveawayInfo.html)


### Example:

```
$payments_giveawayInfoResults = ['_' => 'payments.giveawayInfoResults', 'winner' => Bool, 'refunded' => Bool, 'start_date' => int, 'gift_code_slug' => 'string', 'finish_date' => int, 'winners_count' => int, 'activated_count' => int];
```  
