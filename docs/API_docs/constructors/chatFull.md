---
title: "chatFull"
description: "Detailed chat info"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: chatFull  
[Back to constructors index](/API_docs/constructors/index.md)



Detailed chat info

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|can\_set\_username|[Bool](/API_docs/types/Bool.md) | Optional|Can we change the username of this chat|
|has\_scheduled|[Bool](/API_docs/types/Bool.md) | Optional|Whether [scheduled messages](https://core.telegram.org/api/scheduled-messages) are available|
|id|[long](/API_docs/types/long.md) | Yes|
|about|[string](/API_docs/types/string.md) | Yes|About string for this chat|
|participants|[ChatParticipants](/API_docs/types/ChatParticipants.md) | Yes|Participant list|
|chat\_photo|[Photo](/API_docs/types/Photo.md) | Optional|Chat photo|
|notify\_settings|[PeerNotifySettings](/API_docs/types/PeerNotifySettings.md) | Yes|Notification settings|
|exported\_invite|[ExportedChatInvite](/API_docs/types/ExportedChatInvite.md) | Optional|Chat invite|
|bot\_info|Array of [BotInfo](/API_docs/types/BotInfo.md) | Optional|Info about bots that are in this chat|
|pinned\_msg\_id|[int](/API_docs/types/int.md) | Optional|Message ID of the last [pinned message](https://core.telegram.org/api/pin)|
|folder\_id|[int](/API_docs/types/int.md) | Optional|[Peer folder ID, for more info click here](https://core.telegram.org/api/folders#peer-folders)|
|call|[InputGroupCall](/API_docs/types/InputGroupCall.md) | Optional|
|ttl\_period|[int](/API_docs/types/int.md) | Optional|
|groupcall\_default\_join\_as|[Peer](/API_docs/types/Peer.md) | Optional|
|theme\_emoticon|[string](/API_docs/types/string.md) | Optional|
|requests\_pending|[int](/API_docs/types/int.md) | Optional|
|recent\_requesters|Array of [long](/API_docs/types/long.md) | Optional|
|available\_reactions|Array of [string](/API_docs/types/string.md) | Optional|



### Type: [ChatFull](/API_docs/types/ChatFull.md)


### Example:

```php
$chatFull = ['_' => 'chatFull', 'can_set_username' => Bool, 'has_scheduled' => Bool, 'id' => long, 'about' => 'string', 'participants' => ChatParticipants, 'chat_photo' => Photo, 'notify_settings' => PeerNotifySettings, 'exported_invite' => ExportedChatInvite, 'bot_info' => [BotInfo, BotInfo], 'pinned_msg_id' => int, 'folder_id' => int, 'call' => InputGroupCall, 'ttl_period' => int, 'groupcall_default_join_as' => Peer, 'theme_emoticon' => 'string', 'requests_pending' => int, 'recent_requesters' => [long, long], 'available_reactions' => ['string', 'string']];
```  
