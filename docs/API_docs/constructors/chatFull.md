---
title: "chatFull"
description: "Detailed chat info"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: chatFull  
[Back to constructors index](index.md)



Detailed chat info

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|can\_set\_username|[Bool](../types/Bool.md) | Optional|Can we change the username of this chat|
|has\_scheduled|[Bool](../types/Bool.md) | Optional|Whether [scheduled messages](https://core.telegram.org/api/scheduled-messages) are available|
|id|[long](../types/long.md) | Yes|
|about|[string](../types/string.md) | Yes|About string for this chat|
|participants|[ChatParticipants](../types/ChatParticipants.md) | Yes|Participant list|
|chat\_photo|[Photo](../types/Photo.md) | Optional|Chat photo|
|notify\_settings|[PeerNotifySettings](../types/PeerNotifySettings.md) | Yes|Notification settings|
|exported\_invite|[ExportedChatInvite](../types/ExportedChatInvite.md) | Optional|Chat invite|
|bot\_info|Array of [BotInfo](../types/BotInfo.md) | Optional|Info about bots that are in this chat|
|pinned\_msg\_id|[int](../types/int.md) | Optional|Message ID of the last [pinned message](https://core.telegram.org/api/pin)|
|folder\_id|[int](../types/int.md) | Optional|[Peer folder ID, for more info click here](https://core.telegram.org/api/folders#peer-folders)|
|call|[InputGroupCall](../types/InputGroupCall.md) | Optional|
|ttl\_period|[int](../types/int.md) | Optional|
|groupcall\_default\_join\_as|[Peer](../types/Peer.md) | Optional|
|theme\_emoticon|[string](../types/string.md) | Optional|
|requests\_pending|[int](../types/int.md) | Optional|
|recent\_requesters|Array of [long](../types/long.md) | Optional|



### Type: [ChatFull](../types/ChatFull.md)


### Example:

```php
$chatFull = ['_' => 'chatFull', 'can_set_username' => Bool, 'has_scheduled' => Bool, 'id' => long, 'about' => 'string', 'participants' => ChatParticipants, 'chat_photo' => Photo, 'notify_settings' => PeerNotifySettings, 'exported_invite' => ExportedChatInvite, 'bot_info' => [BotInfo, BotInfo], 'pinned_msg_id' => int, 'folder_id' => int, 'call' => InputGroupCall, 'ttl_period' => int, 'groupcall_default_join_as' => Peer, 'theme_emoticon' => 'string', 'requests_pending' => int, 'recent_requesters' => [long, long]];
```  


Or, if you're into Lua:

```lua
chatFull={_='chatFull', can_set_username=Bool, has_scheduled=Bool, id=long, about='string', participants=ChatParticipants, chat_photo=Photo, notify_settings=PeerNotifySettings, exported_invite=ExportedChatInvite, bot_info={BotInfo}, pinned_msg_id=int, folder_id=int, call=InputGroupCall, ttl_period=int, groupcall_default_join_as=Peer, theme_emoticon='string', requests_pending=int, recent_requesters={long}}

```


