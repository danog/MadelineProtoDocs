---
title: "updateBotMenuButton"
description: "The menu button behavior for the specified bot has changed"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateBotMenuButton  
[Back to constructors index](/API_docs/constructors/index.html)



The menu button behavior for the specified bot has changed

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|bot\_id|[long](/API_docs/types/long.html) | Yes|Bot ID|
|button|[BotMenuButton](/API_docs/types/BotMenuButton.html) | Yes|New menu button|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updateBotMenuButton = ['_' => 'updateBotMenuButton', 'bot_id' => long, 'button' => BotMenuButton];
```  
