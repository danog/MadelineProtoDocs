---
title: "requestPeerTypeBroadcast"
description: "Choose a channel"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: requestPeerTypeBroadcast  
[Back to constructors index](/API_docs/constructors/index.html)



Choose a channel

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|creator|[Bool](/API_docs/types/Bool.html) | Optional|Whether to allow only choosing channels that were created by the current user.|
|has\_username|[Bool](/API_docs/types/Bool.html) | Optional|If specified, allows only choosing channels with or without a username, according to the value of [Bool](../types/Bool.html).|
|user\_admin\_rights|[ChatAdminRights](/API_docs/types/ChatAdminRights.html) | Optional|If specified, allows only choosing channels where the current user is an admin with at least the specified admin rights.|
|bot\_admin\_rights|[ChatAdminRights](/API_docs/types/ChatAdminRights.html) | Optional|If specified, allows only choosing channels where the bot is an admin with at least the specified admin rights.|



### Type: [RequestPeerType](/API_docs/types/RequestPeerType.html)


### Example:

```
$requestPeerTypeBroadcast = ['_' => 'requestPeerTypeBroadcast', 'creator' => Bool, 'has_username' => Bool, 'user_admin_rights' => ChatAdminRights, 'bot_admin_rights' => ChatAdminRights];
```  
