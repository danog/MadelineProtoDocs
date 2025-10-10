---
title: "inputGroupCallInviteMessage"
description: "Join a group call through a messageActionConferenceCall invitation message."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputGroupCallInviteMessage  
[Back to constructors index](/API_docs/constructors/index.html)



Join a group call through a [messageActionConferenceCall](../constructors/messageActionConferenceCall.html) invitation message.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|msg\_id|[int](/API_docs/types/int.html) | Yes|ID of the [messageActionConferenceCall](../constructors/messageActionConferenceCall.html).|



### Type: [InputGroupCall](/API_docs/types/InputGroupCall.html)


### Example:

```
$inputGroupCallInviteMessage = ['_' => 'inputGroupCallInviteMessage', 'msg_id' => int];
```  
