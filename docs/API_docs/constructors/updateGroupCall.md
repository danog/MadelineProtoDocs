---
title: "updateGroupCall"
description: "A new groupcall was started"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateGroupCall  
[Back to constructors index](/API_docs/constructors/index.html)



A new groupcall was started

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|chat\_id|[long](/API_docs/types/long.html) | Yes|The [channel/supergroup](https://core.telegram.org/api/channel) where this group call or livestream takes place|
|call|[GroupCall](/API_docs/types/GroupCall.html) | Yes|Info about the group call or livestream|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updateGroupCall = ['_' => 'updateGroupCall', 'chat_id' => long, 'call' => GroupCall];
```  
