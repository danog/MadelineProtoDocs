---
title: "messageMediaGiveawayResults"
description: "A giveaway with public winners has finished, this constructor contains info about the winners."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageMediaGiveawayResults  
[Back to constructors index](/API_docs/constructors/index.html)



A [giveaway](https://core.telegram.org/api/giveaways) with public winners has finished, this constructor contains info about the winners.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|only\_new\_subscribers|[Bool](/API_docs/types/Bool.html) | Optional|If set, only new subscribers starting from the giveaway creation date participated in the giveaway.|
|refunded|[Bool](/API_docs/types/Bool.html) | Optional|If set, the giveaway was canceled and was fully refunded.|
|channel\_id|[long](/API_docs/types/long.html) | Yes|ID of the channel that was automatically [boosted](https://core.telegram.org/api/boost) by the winners of the giveaway for duration of the Premium subscription.|
|additional\_peers\_count|[int](/API_docs/types/int.html) | Optional|Number of other channels that participated in the giveaway.|
|launch\_msg\_id|[int](/API_docs/types/int.html) | Yes|Identifier of the message with the giveaway in `channel_id`.|
|winners\_count|[int](/API_docs/types/int.html) | Yes|Total number of winners in the giveaway.|
|unclaimed\_count|[int](/API_docs/types/int.html) | Yes|Number of not-yet-claimed prizes.|
|winners|Array of [long](/API_docs/types/long.html) | Yes|Up to 100 user identifiers of the winners of the giveaway.|
|months|[int](/API_docs/types/int.html) | Optional|Duration in months of each [Telegram Premium](https://core.telegram.org/api/premium) subscription in the giveaway.|
|stars|[long](/API_docs/types/long.html) | Optional|
|prize\_description|[string](/API_docs/types/string.html) | Optional|Can contain a textual description of additional giveaway prizes.|
|until\_date|[int](/API_docs/types/int.html) | Yes|Point in time (Unix timestamp) when the winners were selected. May be bigger than winners selection date specified in initial parameters of the giveaway.|



### Type: [MessageMedia](/API_docs/types/MessageMedia.html)


### Example:

```
$messageMediaGiveawayResults = ['_' => 'messageMediaGiveawayResults', 'only_new_subscribers' => Bool, 'refunded' => Bool, 'channel_id' => long, 'additional_peers_count' => int, 'launch_msg_id' => int, 'winners_count' => int, 'unclaimed_count' => int, 'winners' => [long, long], 'months' => int, 'stars' => long, 'prize_description' => 'string', 'until_date' => int];
```  
