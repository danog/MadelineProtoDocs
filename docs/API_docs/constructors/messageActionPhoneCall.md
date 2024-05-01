---
title: "messageActionPhoneCall"
description: "A phone call"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageActionPhoneCall  
[Back to constructors index](/API_docs/constructors/index.html)



A phone call

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|video|[Bool](/API_docs/types/Bool.html) | Optional|Is this a video call?|
|call\_id|[long](/API_docs/types/long.html) | Yes|Call ID|
|reason|[PhoneCallDiscardReason](/API_docs/types/PhoneCallDiscardReason.html) | Optional|If the call has ended, the reason why it ended|
|duration|[int](/API_docs/types/int.html) | Optional|Duration of the call in seconds|



### Type: [MessageAction](/API_docs/types/MessageAction.html)


### Example:

```
$messageActionPhoneCall = ['_' => 'messageActionPhoneCall', 'video' => Bool, 'call_id' => long, 'reason' => PhoneCallDiscardReason, 'duration' => int];
```  
