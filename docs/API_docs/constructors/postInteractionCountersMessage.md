---
title: "postInteractionCountersMessage"
description: "Interaction counters for a message."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: postInteractionCountersMessage  
[Back to constructors index](/API_docs/constructors/index.html)



Interaction counters for a message.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|msg\_id|[int](/API_docs/types/int.html) | Yes|Message ID|
|views|[int](/API_docs/types/int.html) | Yes|Number of views|
|forwards|[int](/API_docs/types/int.html) | Yes|Number of forwards to public channels|
|reactions|[int](/API_docs/types/int.html) | Yes|Number of reactions|



### Type: [PostInteractionCounters](/API_docs/types/PostInteractionCounters.html)


### Example:

```
$postInteractionCountersMessage = ['_' => 'postInteractionCountersMessage', 'msg_id' => int, 'views' => int, 'forwards' => int, 'reactions' => int];
```  
