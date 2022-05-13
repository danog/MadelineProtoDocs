---
title: "chatAdminRights"
description: "Represents the rights of an admin in a channel/supergroup."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: chatAdminRights  
[Back to constructors index](/API_docs/constructors/index.html)



Represents the rights of an admin in a [channel/supergroup](https://core.telegram.org/api/channel).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|change\_info|[Bool](/API_docs/types/Bool.html) | Optional|If set, allows the admin to modify the description of the [channel/supergroup](https://core.telegram.org/api/channel)|
|post\_messages|[Bool](/API_docs/types/Bool.html) | Optional|If set, allows the admin to post messages in the [channel](https://core.telegram.org/api/channel)|
|edit\_messages|[Bool](/API_docs/types/Bool.html) | Optional|If set, allows the admin to also edit messages from other admins in the [channel](https://core.telegram.org/api/channel)|
|delete\_messages|[Bool](/API_docs/types/Bool.html) | Optional|If set, allows the admin to also delete messages from other admins in the [channel](https://core.telegram.org/api/channel)|
|ban\_users|[Bool](/API_docs/types/Bool.html) | Optional|If set, allows the admin to ban users from the [channel/supergroup](https://core.telegram.org/api/channel)|
|invite\_users|[Bool](/API_docs/types/Bool.html) | Optional|If set, allows the admin to invite users in the [channel/supergroup](https://core.telegram.org/api/channel)|
|pin\_messages|[Bool](/API_docs/types/Bool.html) | Optional|If set, allows the admin to pin messages in the [channel/supergroup](https://core.telegram.org/api/channel)|
|add\_admins|[Bool](/API_docs/types/Bool.html) | Optional|If set, allows the admin to add other admins with the same (or more limited) permissions in the [channel/supergroup](https://core.telegram.org/api/channel)|
|anonymous|[Bool](/API_docs/types/Bool.html) | Optional|Whether this admin is anonymous|
|manage\_call|[Bool](/API_docs/types/Bool.html) | Optional|If set, allows the admin to change group call/livestream settings|
|other|[Bool](/API_docs/types/Bool.html) | Optional|Set this flag if none of the other flags are set, but you still want the user to be an admin.|



### Type: [ChatAdminRights](/API_docs/types/ChatAdminRights.html)


### Example:

```
$chatAdminRights = ['_' => 'chatAdminRights', 'change_info' => Bool, 'post_messages' => Bool, 'edit_messages' => Bool, 'delete_messages' => Bool, 'ban_users' => Bool, 'invite_users' => Bool, 'pin_messages' => Bool, 'add_admins' => Bool, 'anonymous' => Bool, 'manage_call' => Bool, 'other' => Bool];
```  
