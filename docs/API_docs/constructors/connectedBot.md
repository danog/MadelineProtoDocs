---
title: "connectedBot"
description: "connectedBot attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: connectedBot  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|can\_reply|[Bool](/API_docs/types/Bool.html) | Optional|
|bot\_id|[long](/API_docs/types/long.html) | Yes|
|recipients|[BusinessBotRecipients](/API_docs/types/BusinessBotRecipients.html) | Yes|



### Type: [ConnectedBot](/API_docs/types/ConnectedBot.html)


### Example:

```
$connectedBot = ['_' => 'connectedBot', 'can_reply' => Bool, 'bot_id' => long, 'recipients' => BusinessBotRecipients];
```  
