---
title: "channelAdminLogEventActionExportedInviteEdit"
description: "A chat invite was edited"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: channelAdminLogEventActionExportedInviteEdit  
[Back to constructors index](/API_docs/constructors/index.html)



A chat invite was edited

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|prev\_invite|[ExportedChatInvite](/API_docs/types/ExportedChatInvite.html) | Yes|Previous chat invite information|
|new\_invite|[ExportedChatInvite](/API_docs/types/ExportedChatInvite.html) | Yes|New chat invite information|



### Type: [ChannelAdminLogEventAction](/API_docs/types/ChannelAdminLogEventAction.html)


### Example:

```
$channelAdminLogEventActionExportedInviteEdit = ['_' => 'channelAdminLogEventActionExportedInviteEdit', 'prev_invite' => ExportedChatInvite, 'new_invite' => ExportedChatInvite];
```  
