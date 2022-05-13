---
title: "channelParticipantCreator"
description: "Channel/supergroup creator"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: channelParticipantCreator  
[Back to constructors index](/API_docs/constructors/index.html)



Channel/supergroup creator

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|user\_id|[long](/API_docs/types/long.html) | Yes|User ID|
|admin\_rights|[ChatAdminRights](/API_docs/types/ChatAdminRights.html) | Yes|Creator admin rights|
|rank|[string](/API_docs/types/string.html) | Optional|The role (rank) of the group creator in the group: just an arbitrary string, `admin` by default|



### Type: [ChannelParticipant](/API_docs/types/ChannelParticipant.html)


### Example:

```
$channelParticipantCreator = ['_' => 'channelParticipantCreator', 'user_id' => long, 'admin_rights' => ChatAdminRights, 'rank' => 'string'];
```  
