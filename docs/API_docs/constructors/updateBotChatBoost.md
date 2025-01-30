---
title: "updateBotChatBoost"
description: "A channel/supergroup boost has changed (bots only)"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateBotChatBoost  
[Back to constructors index](/API_docs/constructors/index.html)



A [channel/supergroup boost](https://core.telegram.org/api/boost) has changed (bots only)

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|peer|[long](/API_docs/types/long.html) | Yes|Channel|
|boost|[Boost](/API_docs/types/Boost.html) | Yes|New boost information|
|qts|[int](/API_docs/types/int.html) | Yes|[QTS](https://core.telegram.org/api/updates) event sequence identifier|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updateBotChatBoost = ['_' => 'updateBotChatBoost', 'peer' => long, 'boost' => Boost, 'qts' => int];
```  
