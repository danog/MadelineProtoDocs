---
title: "chatAdminRights"
description: "Represents the rights of an admin in a channel/supergroup."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: chatAdminRights  
[Back to constructors index](index.md)



Represents the rights of an admin in a [channel/supergroup](https://core.telegram.org/api/channel).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|change\_info|[Bool](../types/Bool.md) | Optional|If set, allows the admin to modify the description of the [channel/supergroup](https://core.telegram.org/api/channel)|
|post\_messages|[Bool](../types/Bool.md) | Optional|If set, allows the admin to post messages in the [channel](https://core.telegram.org/api/channel)|
|edit\_messages|[Bool](../types/Bool.md) | Optional|If set, allows the admin to also edit messages from other admins in the [channel](https://core.telegram.org/api/channel)|
|delete\_messages|[Bool](../types/Bool.md) | Optional|If set, allows the admin to also delete messages from other admins in the [channel](https://core.telegram.org/api/channel)|
|ban\_users|[Bool](../types/Bool.md) | Optional|If set, allows the admin to ban users from the [channel/supergroup](https://core.telegram.org/api/channel)|
|invite\_users|[Bool](../types/Bool.md) | Optional|If set, allows the admin to invite users in the [channel/supergroup](https://core.telegram.org/api/channel)|
|pin\_messages|[Bool](../types/Bool.md) | Optional|If set, allows the admin to pin messages in the [channel/supergroup](https://core.telegram.org/api/channel)|
|add\_admins|[Bool](../types/Bool.md) | Optional|If set, allows the admin to add other admins with the same (or more limited) permissions in the [channel/supergroup](https://core.telegram.org/api/channel)|
|anonymous|[Bool](../types/Bool.md) | Optional|Whether this admin is anonymous|
|manage\_call|[Bool](../types/Bool.md) | Optional|
|other|[Bool](../types/Bool.md) | Optional|



### Type: [ChatAdminRights](../types/ChatAdminRights.md)


### Example:

```php
$chatAdminRights = ['_' => 'chatAdminRights', 'change_info' => Bool, 'post_messages' => Bool, 'edit_messages' => Bool, 'delete_messages' => Bool, 'ban_users' => Bool, 'invite_users' => Bool, 'pin_messages' => Bool, 'add_admins' => Bool, 'anonymous' => Bool, 'manage_call' => Bool, 'other' => Bool];
```  


Or, if you're into Lua:

```lua
chatAdminRights={_='chatAdminRights', change_info=Bool, post_messages=Bool, edit_messages=Bool, delete_messages=Bool, ban_users=Bool, invite_users=Bool, pin_messages=Bool, add_admins=Bool, anonymous=Bool, manage_call=Bool, other=Bool}

```


