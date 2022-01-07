---
title: "chat"
description: "Info about a group"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: chat  
[Back to constructors index](/API_docs/constructors/index.md)



Info about a group

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|creator|[Bool](/API_docs/types/Bool.md) | Optional|Whether the current user is the creator of the group|
|kicked|[Bool](/API_docs/types/Bool.md) | Optional|Whether the current user was kicked from the group|
|left|[Bool](/API_docs/types/Bool.md) | Optional|Whether the current user has left the group|
|deactivated|[Bool](/API_docs/types/Bool.md) | Optional|Whether the group was [migrated](https://core.telegram.org/api/channel)|
|call\_active|[Bool](/API_docs/types/Bool.md) | Optional|
|call\_not\_empty|[Bool](/API_docs/types/Bool.md) | Optional|
|noforwards|[Bool](/API_docs/types/Bool.md) | Optional|
|id|[long](/API_docs/types/long.md) | Yes|
|title|[string](/API_docs/types/string.md) | Yes|Title|
|photo|[ChatPhoto](/API_docs/types/ChatPhoto.md) | Optional|Chat photo|
|participants\_count|[int](/API_docs/types/int.md) | Yes|Participant count|
|date|[int](/API_docs/types/int.md) | Yes|Date of creation of the group|
|version|[int](/API_docs/types/int.md) | Yes|Used in basic groups to reorder updates and make sure that all of them were received.|
|migrated\_to|[InputChannel](/API_docs/types/InputChannel.md) | Optional|Means this chat was [upgraded](https://core.telegram.org/api/channel) to a supergroup|
|admin\_rights|[ChatAdminRights](/API_docs/types/ChatAdminRights.md) | Optional|[Admin rights](https://core.telegram.org/api/rights) of the user in the group|
|default\_banned\_rights|[ChatBannedRights](/API_docs/types/ChatBannedRights.md) | Optional|[Default banned rights](https://core.telegram.org/api/rights) of all users in the group|



### Type: [Chat](/API_docs/types/Chat.md)


### Example:

```php
$chat = ['_' => 'chat', 'creator' => Bool, 'kicked' => Bool, 'left' => Bool, 'deactivated' => Bool, 'call_active' => Bool, 'call_not_empty' => Bool, 'noforwards' => Bool, 'id' => long, 'title' => 'string', 'photo' => ChatPhoto, 'participants_count' => int, 'date' => int, 'version' => int, 'migrated_to' => InputChannel, 'admin_rights' => ChatAdminRights, 'default_banned_rights' => ChatBannedRights];
```  
