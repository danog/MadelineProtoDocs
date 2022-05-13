---
title: "channelAdminLogEventActionExportedInviteDelete"
description: "A chat invite was deleted"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: channelAdminLogEventActionExportedInviteDelete  
[Back to constructors index](/API_docs/constructors/index.html)



A chat invite was deleted

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|invite|[ExportedChatInvite](/API_docs/types/ExportedChatInvite.html) | Yes|The deleted chat invite|



### Type: [ChannelAdminLogEventAction](/API_docs/types/ChannelAdminLogEventAction.html)


### Example:

```
$channelAdminLogEventActionExportedInviteDelete = ['_' => 'channelAdminLogEventActionExportedInviteDelete', 'invite' => ExportedChatInvite];
```  
