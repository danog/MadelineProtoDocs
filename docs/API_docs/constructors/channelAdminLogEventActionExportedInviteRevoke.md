---
title: "channelAdminLogEventActionExportedInviteRevoke"
description: "A specific invite link was revoked"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: channelAdminLogEventActionExportedInviteRevoke  
[Back to constructors index](/API_docs/constructors/index.html)



A specific invite link was revoked

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|invite|[ExportedChatInvite](/API_docs/types/ExportedChatInvite.html) | Yes|The invite link that was revoked|



### Type: [ChannelAdminLogEventAction](/API_docs/types/ChannelAdminLogEventAction.html)


### Example:

```
$channelAdminLogEventActionExportedInviteRevoke = ['_' => 'channelAdminLogEventActionExportedInviteRevoke', 'invite' => ExportedChatInvite];
```  
