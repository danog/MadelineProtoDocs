---
title: "messageActionInviteToGroupCall"
description: "A set of users was invited to the group call"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageActionInviteToGroupCall  
[Back to constructors index](/API_docs/constructors/index.html)



A set of users was invited to the group call

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|call|[InputGroupCall](/API_docs/types/InputGroupCall.html) | Yes|The group call|
|users|Array of [long](/API_docs/types/long.html) | Yes|The invited users|



### Type: [MessageAction](/API_docs/types/MessageAction.html)


### Example:

```
$messageActionInviteToGroupCall = ['_' => 'messageActionInviteToGroupCall', 'call' => InputGroupCall, 'users' => [long, long]];
```  
