---
title: "messageMediaGiveaway"
description: "Contains info about a giveaway, see here » for more info."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageMediaGiveaway  
[Back to constructors index](/API_docs/constructors/index.html)



Contains info about a [giveaway, see here »](https://core.telegram.org/api/giveaways) for more info.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|only\_new\_subscribers|[Bool](/API_docs/types/Bool.html) | Optional|If set, only new subscribers starting from the giveaway creation date will be able to participate to the giveaway.|
|winners\_are\_visible|[Bool](/API_docs/types/Bool.html) | Optional|If set, giveaway winners are public and will be listed in a [messageMediaGiveawayResults](../constructors/messageMediaGiveawayResults.html) message that will be automatically sent to the channel once the giveaway ends.|
|channels|Array of [long](/API_docs/types/long.html) | Yes|The channels that the user must join to participate in the giveaway.|
|countries\_iso2|Array of [string](/API_docs/types/string.html) | Optional|If set, only users residing in these countries can participate in the giveaway, (specified as a list of two-letter ISO 3166-1 alpha-2 country codes); otherwise there are no country-based limitations.|
|prize\_description|[string](/API_docs/types/string.html) | Optional|Can contain a textual description of additional giveaway prizes.|
|quantity|[int](/API_docs/types/int.html) | Yes|Number of [Telegram Premium](https://core.telegram.org/api/premium) subscriptions given away.|
|months|[int](/API_docs/types/int.html) | Optional|Duration in months of each [Telegram Premium](https://core.telegram.org/api/premium) subscription in the giveaway.|
|stars|[long](/API_docs/types/long.html) | Optional|For [Telegram Star giveaways](https://core.telegram.org/api/stars#star-giveaways), the total number of Telegram Stars being given away.|
|until\_date|[int](/API_docs/types/int.html) | Yes|The end date of the giveaway.|



### Type: [MessageMedia](/API_docs/types/MessageMedia.html)


### Example:

```
$messageMediaGiveaway = ['_' => 'messageMediaGiveaway', 'only_new_subscribers' => Bool, 'winners_are_visible' => Bool, 'channels' => [long, long], 'countries_iso2' => ['string', 'string'], 'prize_description' => 'string', 'quantity' => int, 'months' => int, 'stars' => long, 'until_date' => int];
```  
