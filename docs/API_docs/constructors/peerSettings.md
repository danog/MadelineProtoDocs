---
title: "peerSettings"
description: "List of actions that are possible when interacting with this user, to be shown as suggested actions in the chat bar"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: peerSettings  
[Back to constructors index](/API_docs/constructors/index.html)



List of actions that are possible when interacting with this user, to be shown as suggested actions in the chat bar

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|report\_spam|[Bool](/API_docs/types/Bool.html) | Optional|Whether we can still report the user for spam|
|add\_contact|[Bool](/API_docs/types/Bool.html) | Optional|Whether we can add the user as contact|
|block\_contact|[Bool](/API_docs/types/Bool.html) | Optional|Whether we can block the user|
|share\_contact|[Bool](/API_docs/types/Bool.html) | Optional|Whether we can share the user's contact|
|need\_contacts\_exception|[Bool](/API_docs/types/Bool.html) | Optional|Whether a special exception for contacts is needed|
|report\_geo|[Bool](/API_docs/types/Bool.html) | Optional|Whether we can report a geogroup as irrelevant for this location|
|autoarchived|[Bool](/API_docs/types/Bool.html) | Optional|Whether this peer was automatically archived according to [privacy settings](../constructors/globalPrivacySettings.html) and can be unarchived|
|invite\_members|[Bool](/API_docs/types/Bool.html) | Optional|If set, this is a recently created group chat to which new members can be invited|
|request\_chat\_broadcast|[Bool](/API_docs/types/Bool.html) | Optional|This flag is set if `request_chat_title` and `request_chat_date` fields are set and the [join request »](https://core.telegram.org/api/invites#join-requests) is related to a channel (otherwise if only the request fields are set, the [join request »](https://core.telegram.org/api/invites#join-requests) is related to a chat).|
|geo\_distance|[int](/API_docs/types/int.html) | Optional|Distance in meters between us and this peer|
|request\_chat\_title|[string](/API_docs/types/string.html) | Optional|If set, this is a private chat with an administrator of a chat or channel to which the user sent a join request, and this field contains the chat/channel's title.|
|request\_chat\_date|[int](/API_docs/types/int.html) | Optional|If set, this is a private chat with an administrator of a chat or channel to which the user sent a join request, and this field contains the timestamp when the [join request »](https://core.telegram.org/api/invites#join-requests) was sent.|



### Type: [PeerSettings](/API_docs/types/PeerSettings.html)


### Example:

```
$peerSettings = ['_' => 'peerSettings', 'report_spam' => Bool, 'add_contact' => Bool, 'block_contact' => Bool, 'share_contact' => Bool, 'need_contacts_exception' => Bool, 'report_geo' => Bool, 'autoarchived' => Bool, 'invite_members' => Bool, 'request_chat_broadcast' => Bool, 'geo_distance' => int, 'request_chat_title' => 'string', 'request_chat_date' => int];
```  
