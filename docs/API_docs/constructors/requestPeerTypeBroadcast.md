---
title: "requestPeerTypeBroadcast"
description: "requestPeerTypeBroadcast attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: requestPeerTypeBroadcast  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|creator|[Bool](/API_docs/types/Bool.html) | Optional|
|has\_username|[Bool](/API_docs/types/Bool.html) | Optional|
|user\_admin\_rights|[ChatAdminRights](/API_docs/types/ChatAdminRights.html) | Optional|
|bot\_admin\_rights|[ChatAdminRights](/API_docs/types/ChatAdminRights.html) | Optional|



### Type: [RequestPeerType](/API_docs/types/RequestPeerType.html)


### Example:

```
$requestPeerTypeBroadcast = ['_' => 'requestPeerTypeBroadcast', 'creator' => Bool, 'has_username' => Bool, 'user_admin_rights' => ChatAdminRights, 'bot_admin_rights' => ChatAdminRights];
```  
