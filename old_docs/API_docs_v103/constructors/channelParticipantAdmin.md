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
|self|[Bool](../types/Bool.md) | Optional|Is this the current user|
|user\_id|[int](../types/int.md) | Yes|Admin user ID|
|inviter\_id|[int](../types/int.md) | Optional|User that invited the admin to the channel/group|
|promoted\_by|[int](../types/int.md) | Yes|User that promoted the user to admin|
|date|[int](../types/int.md) | Yes|When did the user join|
|admin\_rights|[ChatAdminRights](../types/ChatAdminRights.md) | Yes|Admin [rights](https://core.telegram.org/api/rights)|



### Type: [ChannelParticipant](../types/ChannelParticipant.md)


### Example:

```php
$channelParticipantAdmin = ['_' => 'channelParticipantAdmin', 'can_edit' => Bool, 'self' => Bool, 'user_id' => int, 'inviter_id' => int, 'promoted_by' => int, 'date' => int, 'admin_rights' => ChatAdminRights];
```  


Or, if you're into Lua:

```lua
channelParticipantAdmin={_='channelParticipantAdmin', can_edit=Bool, self=Bool, user_id=int, inviter_id=int, promoted_by=int, date=int, admin_rights=ChatAdminRights}

```


