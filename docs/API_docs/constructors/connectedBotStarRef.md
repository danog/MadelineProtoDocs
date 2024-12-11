---
title: "connectedBotStarRef"
description: "connectedBotStarRef attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: connectedBotStarRef  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|revoked|[Bool](/API_docs/types/Bool.html) | Optional|
|url|[string](/API_docs/types/string.html) | Yes|
|date|[int](/API_docs/types/int.html) | Yes|
|bot\_id|[long](/API_docs/types/long.html) | Yes|
|commission\_permille|[int](/API_docs/types/int.html) | Yes|
|duration\_months|[int](/API_docs/types/int.html) | Optional|
|participants|[long](/API_docs/types/long.html) | Yes|
|revenue|[long](/API_docs/types/long.html) | Yes|



### Type: [ConnectedBotStarRef](/API_docs/types/ConnectedBotStarRef.html)


### Example:

```
$connectedBotStarRef = ['_' => 'connectedBotStarRef', 'revoked' => Bool, 'url' => 'string', 'date' => int, 'bot_id' => long, 'commission_permille' => int, 'duration_months' => int, 'participants' => long, 'revenue' => long];
```  
