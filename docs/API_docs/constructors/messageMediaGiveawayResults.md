---
title: "messageMediaGiveawayResults"
description: "messageMediaGiveawayResults attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageMediaGiveawayResults  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|only\_new\_subscribers|[Bool](/API_docs/types/Bool.html) | Optional|
|refunded|[Bool](/API_docs/types/Bool.html) | Optional|
|channel\_id|[long](/API_docs/types/long.html) | Yes|
|additional\_peers\_count|[int](/API_docs/types/int.html) | Optional|
|launch\_msg\_id|[int](/API_docs/types/int.html) | Yes|
|winners\_count|[int](/API_docs/types/int.html) | Yes|
|unclaimed\_count|[int](/API_docs/types/int.html) | Yes|
|winners|Array of [long](/API_docs/types/long.html) | Yes|
|months|[int](/API_docs/types/int.html) | Yes|
|prize\_description|[string](/API_docs/types/string.html) | Optional|
|until\_date|[int](/API_docs/types/int.html) | Yes|



### Type: [MessageMedia](/API_docs/types/MessageMedia.html)


### Example:

```
$messageMediaGiveawayResults = ['_' => 'messageMediaGiveawayResults', 'only_new_subscribers' => Bool, 'refunded' => Bool, 'channel_id' => long, 'additional_peers_count' => int, 'launch_msg_id' => int, 'winners_count' => int, 'unclaimed_count' => int, 'winners' => [long, long], 'months' => int, 'prize_description' => 'string', 'until_date' => int];
```  
