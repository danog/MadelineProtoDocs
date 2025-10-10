---
title: "botVerification"
description: "Describes a bot verification icon »."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: botVerification  
[Back to constructors index](/API_docs/constructors/index.html)



Describes a [bot verification icon »](https://core.telegram.org/api/bots/verification).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|bot\_id|[long](/API_docs/types/long.html) | Yes|ID of the bot that verified this peer|
|icon|[long](/API_docs/types/long.html) | Yes|Verification icon|
|description|[string](/API_docs/types/string.html) | Yes|Verification description|



### Type: [BotVerification](/API_docs/types/BotVerification.html)


### Example:

```
$botVerification = ['_' => 'botVerification', 'bot_id' => long, 'icon' => long, 'description' => 'string'];
```  
