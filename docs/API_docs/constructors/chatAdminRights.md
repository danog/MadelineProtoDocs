---
title: chatAdminRights
description: chatAdminRights attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: chatAdminRights  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|change\_info|[Bool](../types/Bool.md) | Optional|
|post\_messages|[Bool](../types/Bool.md) | Optional|
|edit\_messages|[Bool](../types/Bool.md) | Optional|
|delete\_messages|[Bool](../types/Bool.md) | Optional|
|ban\_users|[Bool](../types/Bool.md) | Optional|
|invite\_users|[Bool](../types/Bool.md) | Optional|
|pin\_messages|[Bool](../types/Bool.md) | Optional|
|add\_admins|[Bool](../types/Bool.md) | Optional|



### Type: [ChatAdminRights](../types/ChatAdminRights.md)


### Example:

```php
$chatAdminRights = ['_' => 'chatAdminRights', 'change_info' => Bool, 'post_messages' => Bool, 'edit_messages' => Bool, 'delete_messages' => Bool, 'ban_users' => Bool, 'invite_users' => Bool, 'pin_messages' => Bool, 'add_admins' => Bool];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "chatAdminRights", "change_info": Bool, "post_messages": Bool, "edit_messages": Bool, "delete_messages": Bool, "ban_users": Bool, "invite_users": Bool, "pin_messages": Bool, "add_admins": Bool}
```


Or, if you're into Lua:

```lua
chatAdminRights={_='chatAdminRights', change_info=Bool, post_messages=Bool, edit_messages=Bool, delete_messages=Bool, ban_users=Bool, invite_users=Bool, pin_messages=Bool, add_admins=Bool}

```


