---
title: "updateBotChatBoost"
description: "updateBotChatBoost attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateBotChatBoost  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|peer|[long](/API_docs/types/long.html) | Yes|
|boost|[Boost](/API_docs/types/Boost.html) | Yes|
|qts|[int](/API_docs/types/int.html) | Yes|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updateBotChatBoost = ['_' => 'updateBotChatBoost', 'peer' => long, 'boost' => Boost, 'qts' => int];
```  
