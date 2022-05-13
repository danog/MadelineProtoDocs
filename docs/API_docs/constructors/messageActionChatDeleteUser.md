---
title: "messageActionChatDeleteUser"
description: "User left the group."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageActionChatDeleteUser  
[Back to constructors index](/API_docs/constructors/index.html)



User left the group.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|user\_id|[long](/API_docs/types/long.html) | Yes|Leaving user ID|



### Type: [MessageAction](/API_docs/types/MessageAction.html)


### Example:

```
$messageActionChatDeleteUser = ['_' => 'messageActionChatDeleteUser', 'user_id' => long];
```  
