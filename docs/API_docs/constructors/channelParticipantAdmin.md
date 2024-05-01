---
title: "channelParticipantAdmin"
description: "Admin"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: channelParticipantAdmin  
[Back to constructors index](/API_docs/constructors/index.html)



Admin

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|can\_edit|[Bool](/API_docs/types/Bool.html) | Optional|Can this admin promote other admins with the same permissions?|
|self|[Bool](/API_docs/types/Bool.html) | Optional|Is this the current user|
|user\_id|[long](/API_docs/types/long.html) | Yes|Admin user ID|
|inviter\_id|[long](/API_docs/types/long.html) | Optional|User that invited the admin to the channel/group|
|promoted\_by|[long](/API_docs/types/long.html) | Yes|User that promoted the user to admin|
|date|[int](/API_docs/types/int.html) | Yes|When did the user join|
|admin\_rights|[ChatAdminRights](/API_docs/types/ChatAdminRights.html) | Yes|Admin [rights](https://core.telegram.org/api/rights)|
|rank|[string](/API_docs/types/string.html) | Optional|The role (rank) of the admin in the group: just an arbitrary string, `admin` by default|



### Type: [ChannelParticipant](/API_docs/types/ChannelParticipant.html)


### Example:

```
$channelParticipantAdmin = ['_' => 'channelParticipantAdmin', 'can_edit' => Bool, 'self' => Bool, 'user_id' => long, 'inviter_id' => long, 'promoted_by' => long, 'date' => int, 'admin_rights' => ChatAdminRights, 'rank' => 'string'];
```  
