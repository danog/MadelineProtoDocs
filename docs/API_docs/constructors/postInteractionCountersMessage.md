---
title: "postInteractionCountersMessage"
description: "postInteractionCountersMessage attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: postInteractionCountersMessage  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|msg\_id|[int](/API_docs/types/int.html) | Yes|
|views|[int](/API_docs/types/int.html) | Yes|
|forwards|[int](/API_docs/types/int.html) | Yes|
|reactions|[int](/API_docs/types/int.html) | Yes|



### Type: [PostInteractionCounters](/API_docs/types/PostInteractionCounters.html)


### Example:

```
$postInteractionCountersMessage = ['_' => 'postInteractionCountersMessage', 'msg_id' => int, 'views' => int, 'forwards' => int, 'reactions' => int];
```  
