---
title: "messageActionGiveawayLaunch"
description: "A giveaway was started."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageActionGiveawayLaunch  
[Back to constructors index](/API_docs/constructors/index.html)



A [giveaway](https://core.telegram.org/api/giveaways) was started.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|stars|[long](/API_docs/types/long.html) | Optional|For [Telegram Star giveaways](https://core.telegram.org/api/stars#star-giveaways), the total number of Telegram Stars being given away.|



### Type: [MessageAction](/API_docs/types/MessageAction.html)


### Example:

```
$messageActionGiveawayLaunch = ['_' => 'messageActionGiveawayLaunch', 'stars' => long];
```  
