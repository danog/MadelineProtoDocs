---
title: channelParticipantAdmin
description: Channel participant admin
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: channelParticipantAdmin  
[Back to constructors index](index.md)



Channel participant admin

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|can\_edit|[Bool](../types/Bool.md) | Optional|Can edit?|
|self|[Bool](../types/Bool.md) | Optional|Is this the current user?|
|user\_id|[int](../types/int.md) | Yes|User ID|
|inviter\_id|[int](../types/int.md) | Optional|Inviter ID|
|promoted\_by|[int](../types/int.md) | Yes|Promoted by|
|date|[int](../types/int.md) | Yes|Date|
|admin\_rights|[ChatAdminRights](../types/ChatAdminRights.md) | Yes|Admin rights|
|rank|[string](../types/string.md) | Optional|Admin's rank, an arbitrary string|



### Type: [ChannelParticipant](../types/ChannelParticipant.md)


### Example:

```php
$channelParticipantAdmin = ['_' => 'channelParticipantAdmin', 'can_edit' => Bool, 'self' => Bool, 'user_id' => int, 'inviter_id' => int, 'promoted_by' => int, 'date' => int, 'admin_rights' => ChatAdminRights, 'rank' => 'string'];
```  


Or, if you're into Lua:

```lua
channelParticipantAdmin={_='channelParticipantAdmin', can_edit=Bool, self=Bool, user_id=int, inviter_id=int, promoted_by=int, date=int, admin_rights=ChatAdminRights, rank='string'}

```


