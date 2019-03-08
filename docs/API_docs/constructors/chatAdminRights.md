---
title: chatAdminRights
description: Admin rights
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: chatAdminRights  
[Back to constructors index](index.md)



Admin rights

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|change\_info|[Bool](../types/Bool.md) | Optional|Can change info?|
|post\_messages|[Bool](../types/Bool.md) | Optional|Can post messages?|
|edit\_messages|[Bool](../types/Bool.md) | Optional|Can edit messages?|
|delete\_messages|[Bool](../types/Bool.md) | Optional|Can delete messages?|
|ban\_users|[Bool](../types/Bool.md) | Optional|Can ban users?|
|invite\_users|[Bool](../types/Bool.md) | Optional|Can invite users?|
|pin\_messages|[Bool](../types/Bool.md) | Optional|Can pin messages?|
|add\_admins|[Bool](../types/Bool.md) | Optional|Can add other admins?|



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


