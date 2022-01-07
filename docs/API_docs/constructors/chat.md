---
title: "chat"
description: "Info about a group"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: chat  
[Back to constructors index](index.md)



Info about a group

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|creator|[Bool](../types/Bool.md) | Optional|Whether the current user is the creator of the group|
|kicked|[Bool](../types/Bool.md) | Optional|Whether the current user was kicked from the group|
|left|[Bool](../types/Bool.md) | Optional|Whether the current user has left the group|
|deactivated|[Bool](../types/Bool.md) | Optional|Whether the group was [migrated](https://core.telegram.org/api/channel)|
|call\_active|[Bool](../types/Bool.md) | Optional|
|call\_not\_empty|[Bool](../types/Bool.md) | Optional|
|noforwards|[Bool](../types/Bool.md) | Optional|
|id|[long](../types/long.md) | Yes|
|title|[string](../types/string.md) | Yes|Title|
|photo|[ChatPhoto](../types/ChatPhoto.md) | Optional|Chat photo|
|participants\_count|[int](../types/int.md) | Yes|Participant count|
|date|[int](../types/int.md) | Yes|Date of creation of the group|
|version|[int](../types/int.md) | Yes|Used in basic groups to reorder updates and make sure that all of them were received.|
|migrated\_to|[InputChannel](../types/InputChannel.md) | Optional|Means this chat was [upgraded](https://core.telegram.org/api/channel) to a supergroup|
|admin\_rights|[ChatAdminRights](../types/ChatAdminRights.md) | Optional|[Admin rights](https://core.telegram.org/api/rights) of the user in the group|
|default\_banned\_rights|[ChatBannedRights](../types/ChatBannedRights.md) | Optional|[Default banned rights](https://core.telegram.org/api/rights) of all users in the group|



### Type: [Chat](../types/Chat.md)


### Example:

```php
$chat = ['_' => 'chat', 'creator' => Bool, 'kicked' => Bool, 'left' => Bool, 'deactivated' => Bool, 'call_active' => Bool, 'call_not_empty' => Bool, 'noforwards' => Bool, 'id' => long, 'title' => 'string', 'photo' => ChatPhoto, 'participants_count' => int, 'date' => int, 'version' => int, 'migrated_to' => InputChannel, 'admin_rights' => ChatAdminRights, 'default_banned_rights' => ChatBannedRights];
```  
