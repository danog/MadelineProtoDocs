---
title: "chatFull"
description: "Detailed chat info"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: chatFull  
[Back to constructors index](/API_docs/constructors/index.html)



Detailed chat info

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|can\_set\_username|[Bool](/API_docs/types/Bool.html) | Optional|Can we change the username of this chat|
|has\_scheduled|[Bool](/API_docs/types/Bool.html) | Optional|Whether [scheduled messages](https://core.telegram.org/api/scheduled-messages) are available|
|id|[long](/API_docs/types/long.html) | Yes|
|about|[string](/API_docs/types/string.html) | Yes|About string for this chat|
|participants|[ChatParticipants](/API_docs/types/ChatParticipants.html) | Yes|Participant list|
|chat\_photo|[Photo](/API_docs/types/Photo.html) | Optional|Chat photo|
|notify\_settings|[PeerNotifySettings](/API_docs/types/PeerNotifySettings.html) | Yes|Notification settings|
|exported\_invite|[ExportedChatInvite](/API_docs/types/ExportedChatInvite.html) | Optional|Chat invite|
|bot\_info|Array of [BotInfo](/API_docs/types/BotInfo.html) | Optional|Info about bots that are in this chat|
|pinned\_msg\_id|[int](/API_docs/types/int.html) | Optional|Message ID of the last [pinned message](https://core.telegram.org/api/pin)|
|folder\_id|[int](/API_docs/types/int.html) | Optional|[Peer folder ID, for more info click here](https://core.telegram.org/api/folders#peer-folders)|
|call|[InputGroupCall](/API_docs/types/InputGroupCall.html) | Optional|
|ttl\_period|[int](/API_docs/types/int.html) | Optional|
|groupcall\_default\_join\_as|[Peer](/API_docs/types/Peer.html) | Optional|
|theme\_emoticon|[string](/API_docs/types/string.html) | Optional|
|requests\_pending|[int](/API_docs/types/int.html) | Optional|
|recent\_requesters|Array of [long](/API_docs/types/long.html) | Optional|
|available\_reactions|Array of [string](/API_docs/types/string.html) | Optional|



### Type: [ChatFull](/API_docs/types/ChatFull.html)


### Example:

```php
$chatFull = ['_' => 'chatFull', 'can_set_username' => Bool, 'has_scheduled' => Bool, 'id' => long, 'about' => 'string', 'participants' => ChatParticipants, 'chat_photo' => Photo, 'notify_settings' => PeerNotifySettings, 'exported_invite' => ExportedChatInvite, 'bot_info' => [BotInfo, BotInfo], 'pinned_msg_id' => int, 'folder_id' => int, 'call' => InputGroupCall, 'ttl_period' => int, 'groupcall_default_join_as' => Peer, 'theme_emoticon' => 'string', 'requests_pending' => int, 'recent_requesters' => [long, long], 'available_reactions' => ['string', 'string']];
```  
