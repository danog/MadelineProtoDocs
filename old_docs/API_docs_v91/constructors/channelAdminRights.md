---
title: channelAdminRights
description: Admin rights
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: channelAdminRights  
[Back to constructors index](index.md)



Admin rights

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|change\_info|[Bool](../types/Bool.md) | Optional|Change info|
|post\_messages|[Bool](../types/Bool.md) | Optional|Post messages|
|edit\_messages|[Bool](../types/Bool.md) | Optional|Edit messages|
|delete\_messages|[Bool](../types/Bool.md) | Optional|Delete messages|
|ban\_users|[Bool](../types/Bool.md) | Optional|Ban users|
|invite\_users|[Bool](../types/Bool.md) | Optional|Invite users|
|invite\_link|[Bool](../types/Bool.md) | Optional|Generate an invite link|
|pin\_messages|[Bool](../types/Bool.md) | Optional|Pin messages|
|add\_admins|[Bool](../types/Bool.md) | Optional|Add other admins|
|manage\_call|[Bool](../types/Bool.md) | Optional|Manage group calls|



### Type: [ChannelAdminRights](../types/ChannelAdminRights.md)


### Example:

```php
$channelAdminRights = ['_' => 'channelAdminRights', 'change_info' => Bool, 'post_messages' => Bool, 'edit_messages' => Bool, 'delete_messages' => Bool, 'ban_users' => Bool, 'invite_users' => Bool, 'invite_link' => Bool, 'pin_messages' => Bool, 'add_admins' => Bool, 'manage_call' => Bool];
```  


Or, if you're into Lua:

```lua
channelAdminRights={_='channelAdminRights', change_info=Bool, post_messages=Bool, edit_messages=Bool, delete_messages=Bool, ban_users=Bool, invite_users=Bool, invite_link=Bool, pin_messages=Bool, add_admins=Bool, manage_call=Bool}

```


