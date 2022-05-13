---
title: "chatInviteImporter"
description: "When and which user joined the chat using a chat invite"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: chatInviteImporter  
[Back to constructors index](/API_docs/constructors/index.html)



When and which user joined the chat using a chat invite

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|requested|[Bool](/API_docs/types/Bool.html) | Optional|Whether this user currently has a pending [join request »](https://core.telegram.org/api/invites#join-requests)|
|user\_id|[long](/API_docs/types/long.html) | Yes|The user|
|date|[int](/API_docs/types/int.html) | Yes|When did the user join|
|about|[string](/API_docs/types/string.html) | Optional|For users with pending requests, contains bio of the user that requested to join|
|approved\_by|[long](/API_docs/types/long.html) | Optional|The administrator that approved the [join request »](https://core.telegram.org/api/invites#join-requests) of the user|



### Type: [ChatInviteImporter](/API_docs/types/ChatInviteImporter.html)


### Example:

```
$chatInviteImporter = ['_' => 'chatInviteImporter', 'requested' => Bool, 'user_id' => long, 'date' => int, 'about' => 'string', 'approved_by' => long];
```  
