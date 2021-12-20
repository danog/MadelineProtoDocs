---
title: "channelParticipantAdmin"
description: "Admin"
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
|user\_id|[long](../types/long.md) | Yes|
|inviter\_id|[long](../types/long.md) | Optional|
|promoted\_by|[long](../types/long.md) | Yes|
|date|[int](../types/int.md) | Yes|When did the user join|
|admin\_rights|[ChatAdminRights](../types/ChatAdminRights.md) | Yes|Admin [rights](https://core.telegram.org/api/rights)|
|rank|[string](../types/string.md) | Optional|The role (rank) of the admin in the group: just an arbitrary string, `admin` by default|



### Type: [ChannelParticipant](../types/ChannelParticipant.md)


### Example:

```php
$channelParticipantAdmin = ['_' => 'channelParticipantAdmin', 'can_edit' => Bool, 'self' => Bool, 'user_id' => long, 'inviter_id' => long, 'promoted_by' => long, 'date' => int, 'admin_rights' => ChatAdminRights, 'rank' => 'string'];
```  


Or, if you're into Lua:

```lua
channelParticipantAdmin={_='channelParticipantAdmin', can_edit=Bool, self=Bool, user_id=long, inviter_id=long, promoted_by=long, date=int, admin_rights=ChatAdminRights, rank='string'}

```


