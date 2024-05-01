---
title: "encryptedChatWaiting"
description: "Chat waiting for approval of second participant."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: encryptedChatWaiting  
[Back to constructors index](/API_docs/constructors/index.html)



Chat waiting for approval of second participant.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[int](/API_docs/types/int.html) | Yes|Chat ID|
|access\_hash|[long](/API_docs/types/long.html) | Yes|Checking sum depending on user ID|
|date|[int](/API_docs/types/int.html) | Yes|Date of chat creation|
|admin\_id|[long](/API_docs/types/long.html) | Yes|Chat creator ID|
|participant\_id|[long](/API_docs/types/long.html) | Yes|ID of second chat participant|



### Type: [EncryptedChat](/API_docs/types/EncryptedChat.html)


### Example:

```
$encryptedChatWaiting = ['_' => 'encryptedChatWaiting', 'id' => int, 'access_hash' => long, 'date' => int, 'admin_id' => long, 'participant_id' => long];
```  
