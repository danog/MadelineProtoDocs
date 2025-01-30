---
title: "messageActionBoostApply"
description: "Some boosts » were applied to the channel or supergroup."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageActionBoostApply  
[Back to constructors index](/API_docs/constructors/index.html)



Some [boosts »](https://core.telegram.org/api/boost) were applied to the channel or supergroup.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|boosts|[int](/API_docs/types/int.html) | Yes|Number of applied [boosts](https://core.telegram.org/api/boost).|



### Type: [MessageAction](/API_docs/types/MessageAction.html)


### Example:

```
$messageActionBoostApply = ['_' => 'messageActionBoostApply', 'boosts' => int];
```  
