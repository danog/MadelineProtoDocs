---
title: "chat"
description: "Info about a group."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: chat  
[Back to constructors index](/API_docs/constructors/index.html)



Info about a group.

When updating the [local peer database](https://core.telegram.org/api/peers), all fields from the newly received constructor take priority over the old constructor cached locally (including by removing fields that aren't set in the new constructor).

See [here »](https://github.com/tdlib/td/blob/a24af0992245f838f2b4b418a0a2d5fa9caa27b5/td/telegram/ChatManager.cpp#L5152) for an implementation of the logic to use when updating the [local user peer database](https://core.telegram.org/api/peers).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|creator|[Bool](/API_docs/types/Bool.html) | Optional|Whether the current user is the creator of the group|
|left|[Bool](/API_docs/types/Bool.html) | Optional|Whether the current user has left the group|
|deactivated|[Bool](/API_docs/types/Bool.html) | Optional|Whether the group was [migrated](https://core.telegram.org/api/channel)|
|call\_active|[Bool](/API_docs/types/Bool.html) | Optional|Whether a group call is currently active|
|call\_not\_empty|[Bool](/API_docs/types/Bool.html) | Optional|Whether there's anyone in the group call|
|noforwards|[Bool](/API_docs/types/Bool.html) | Optional|Whether this group is [protected](https://telegram.org/blog/protected-content-delete-by-date-and-more), thus does not allow forwarding messages from it|
|id|[long](/API_docs/types/long.html) | Yes|ID of the group, see [here »](https://core.telegram.org/api/peers#peer-id) for more info and the available ID range.|
|title|[string](/API_docs/types/string.html) | Yes|Title|
|photo|[ChatPhoto](/API_docs/types/ChatPhoto.html) | Optional|Chat photo|
|participants\_count|[int](/API_docs/types/int.html) | Yes|Participant count|
|date|[int](/API_docs/types/int.html) | Yes|Date of creation of the group|
|version|[int](/API_docs/types/int.html) | Yes|Used in basic groups to reorder updates and make sure that all of them were received.|
|migrated\_to|[InputChannel](/API_docs/types/InputChannel.html) | Optional|Means this chat was [upgraded](https://core.telegram.org/api/channel) to a supergroup|
|admin\_rights|[ChatAdminRights](/API_docs/types/ChatAdminRights.html) | Optional|[Admin rights](https://core.telegram.org/api/rights) of the user in the group|
|default\_banned\_rights|[ChatBannedRights](/API_docs/types/ChatBannedRights.html) | Optional|[Default banned rights](https://core.telegram.org/api/rights) of all users in the group|



### Type: [Chat](/API_docs/types/Chat.html)


### Example:

```
$chat = ['_' => 'chat', 'creator' => Bool, 'left' => Bool, 'deactivated' => Bool, 'call_active' => Bool, 'call_not_empty' => Bool, 'noforwards' => Bool, 'id' => long, 'title' => 'string', 'photo' => ChatPhoto, 'participants_count' => int, 'date' => int, 'version' => int, 'migrated_to' => InputChannel, 'admin_rights' => ChatAdminRights, 'default_banned_rights' => ChatBannedRights];
```  
