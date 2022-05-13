---
title: "messages.affectedMessages"
description: "Events affected by operation"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/messages_affectedMessages.html
---
# Constructor: messages.affectedMessages  
[Back to constructors index](/API_docs/constructors/index.html)



Events affected by operation

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|pts|[int](/API_docs/types/int.html) | Yes|[Event count after generation](https://core.telegram.org/api/updates)|
|pts\_count|[int](/API_docs/types/int.html) | Yes|[Number of events that were generated](https://core.telegram.org/api/updates)|



### Type: [messages.AffectedMessages](/API_docs/types/messages.AffectedMessages.html)


### Example:

```
$messages_affectedMessages = ['_' => 'messages.affectedMessages', 'pts' => int, 'pts_count' => int];
```  
