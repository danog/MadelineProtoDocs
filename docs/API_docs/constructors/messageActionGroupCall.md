---
title: "messageActionGroupCall"
description: "The group call has ended"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageActionGroupCall  
[Back to constructors index](/API_docs/constructors/index.html)



The group call has ended

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|call|[InputGroupCall](/API_docs/types/InputGroupCall.html) | Yes|Group call|
|duration|[int](/API_docs/types/int.html) | Optional|Group call duration|



### Type: [MessageAction](/API_docs/types/MessageAction.html)


### Example:

```
$messageActionGroupCall = ['_' => 'messageActionGroupCall', 'call' => InputGroupCall, 'duration' => int];
```  
