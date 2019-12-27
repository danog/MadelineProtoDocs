---
title: channelParticipantAdmin
description: Admin
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: channelParticipantAdmin  
[Back to constructors index](index.md)



Admin

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|can\_edit|[Bool](../types/Bool.md) | Optional|Can this admin promote other admins with the same permissions?|
|user\_id|[int](../types/int.md) | Yes|Admin user ID|
|inviter\_id|[int](../types/int.md) | Yes|User that invited the admin to the channel/group|
|promoted\_by|[int](../types/int.md) | Yes|User that promoted the user to admin|
|date|[int](../types/int.md) | Yes|When did the user join|
|admin\_rights|[ChannelAdminRights](../types/ChannelAdminRights.md) | Yes|Admin rights|



### Type: [ChannelParticipant](../types/ChannelParticipant.md)


### Example:

```php
$channelParticipantAdmin = ['_' => 'channelParticipantAdmin', 'can_edit' => Bool, 'user_id' => int, 'inviter_id' => int, 'promoted_by' => int, 'date' => int, 'admin_rights' => ChannelAdminRights];
```  


Or, if you're into Lua:

```lua
channelParticipantAdmin={_='channelParticipantAdmin', can_edit=Bool, user_id=int, inviter_id=int, promoted_by=int, date=int, admin_rights=ChannelAdminRights}

```


