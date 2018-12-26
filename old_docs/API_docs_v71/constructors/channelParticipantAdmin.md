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
|user\_id|[int](../types/int.md) | Yes|User ID|
|inviter\_id|[int](../types/int.md) | Yes|Inviter ID|
|promoted\_by|[int](../types/int.md) | Yes|Promoted by|
|date|[int](../types/int.md) | Yes|Date|
|admin\_rights|[ChannelAdminRights](../types/ChannelAdminRights.md) | Yes|Admin rights|



### Type: [ChannelParticipant](../types/ChannelParticipant.md)


### Example:

```php
$channelParticipantAdmin = ['_' => 'channelParticipantAdmin', 'can_edit' => Bool, 'user_id' => int, 'inviter_id' => int, 'promoted_by' => int, 'date' => int, 'admin_rights' => ChannelAdminRights];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "channelParticipantAdmin", "can_edit": Bool, "user_id": int, "inviter_id": int, "promoted_by": int, "date": int, "admin_rights": ChannelAdminRights}
```


Or, if you're into Lua:

```lua
channelParticipantAdmin={_='channelParticipantAdmin', can_edit=Bool, user_id=int, inviter_id=int, promoted_by=int, date=int, admin_rights=ChannelAdminRights}

```


