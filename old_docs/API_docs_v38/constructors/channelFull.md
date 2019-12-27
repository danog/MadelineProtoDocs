---
title: channelFull
description: Full info about a [channel/supergroup](https://core.telegram.org/api/channel)
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: channelFull  
[Back to constructors index](index.md)



Full info about a [channel/supergroup](https://core.telegram.org/api/channel)

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[int](../types/int.md) | Yes|ID of the channel|
|about|[string](../types/string.md) | Yes|Info about the channel|
|participants\_count|[int](../types/int.md) | Optional|Number of participants of the channel|
|admins\_count|[int](../types/int.md) | Optional|Number of channel admins|
|kicked\_count|[int](../types/int.md) | Optional|Number of users [kicked](https://core.telegram.org/api/rights) from the channel|
|read\_inbox\_max\_id|[int](../types/int.md) | Yes|Position up to which all incoming messages are read.|
|unread\_count|[int](../types/int.md) | Yes|Count of unread messages|
|unread\_important\_count|[int](../types/int.md) | Yes|Unread important count|
|chat\_photo|[Photo](../types/Photo.md) | Optional|Channel picture|
|notify\_settings|[PeerNotifySettings](../types/PeerNotifySettings.md) | Optional|Notification settings|
|exported\_invite|[ExportedChatInvite](../types/ExportedChatInvite.md) | Yes|Invite link|



### Type: [ChatFull](../types/ChatFull.md)


### Example:

```php
$channelFull = ['_' => 'channelFull', 'id' => int, 'about' => 'string', 'participants_count' => int, 'admins_count' => int, 'kicked_count' => int, 'read_inbox_max_id' => int, 'unread_count' => int, 'unread_important_count' => int, 'chat_photo' => Photo, 'notify_settings' => PeerNotifySettings, 'exported_invite' => ExportedChatInvite];
```  


Or, if you're into Lua:

```lua
channelFull={_='channelFull', id=int, about='string', participants_count=int, admins_count=int, kicked_count=int, read_inbox_max_id=int, unread_count=int, unread_important_count=int, chat_photo=Photo, notify_settings=PeerNotifySettings, exported_invite=ExportedChatInvite}

```


