---
title: "requestPeerTypeChat"
description: "Choose a chat or supergroup"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: requestPeerTypeChat  
[Back to constructors index](/API_docs/constructors/index.html)



Choose a chat or supergroup

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|creator|[Bool](/API_docs/types/Bool.html) | Optional|Whether to allow only choosing chats or supergroups that were created by the current user.|
|bot\_participant|[Bool](/API_docs/types/Bool.html) | Optional|Whether to allow only choosing chats or supergroups where the bot is a participant.|
|has\_username|[Bool](/API_docs/types/Bool.html) | Optional|If specified, allows only choosing channels with or without a username, according to the value of [Bool](../types/Bool.html).|
|forum|[Bool](/API_docs/types/Bool.html) | Optional|If specified, allows only choosing chats or supergroups that are or aren't [forums](https://core.telegram.org/api/forum), according to the value of [Bool](../types/Bool.html).|
|user\_admin\_rights|[ChatAdminRights](/API_docs/types/ChatAdminRights.html) | Optional|If specified, allows only choosing chats or supergroups where the current user is an admin with at least the specified admin rights.|
|bot\_admin\_rights|[ChatAdminRights](/API_docs/types/ChatAdminRights.html) | Optional|If specified, allows only choosing chats or supergroups where the bot is an admin with at least the specified admin rights.|



### Type: [RequestPeerType](/API_docs/types/RequestPeerType.html)


### Example:

```
$requestPeerTypeChat = ['_' => 'requestPeerTypeChat', 'creator' => Bool, 'bot_participant' => Bool, 'has_username' => Bool, 'forum' => Bool, 'user_admin_rights' => ChatAdminRights, 'bot_admin_rights' => ChatAdminRights];
```  
