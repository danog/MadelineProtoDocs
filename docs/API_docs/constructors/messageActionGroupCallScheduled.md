---
title: "messageActionGroupCallScheduled"
description: "A group call was scheduled"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageActionGroupCallScheduled  
[Back to constructors index](/API_docs/constructors/index.html)



A group call was scheduled

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|call|[InputGroupCall](/API_docs/types/InputGroupCall.html) | Yes|The group call|
|schedule\_date|[int](/API_docs/types/int.html) | Yes|When is this group call scheduled to start|



### Type: [MessageAction](/API_docs/types/MessageAction.html)


### Example:

```
$messageActionGroupCallScheduled = ['_' => 'messageActionGroupCallScheduled', 'call' => InputGroupCall, 'schedule_date' => int];
```  
