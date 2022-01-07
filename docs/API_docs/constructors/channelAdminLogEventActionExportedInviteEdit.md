---
title: "channelAdminLogEventActionExportedInviteEdit"
description: "channelAdminLogEventActionExportedInviteEdit attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: channelAdminLogEventActionExportedInviteEdit  
[Back to constructors index](/API_docs/constructors/index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|prev\_invite|[ExportedChatInvite](/API_docs/types/ExportedChatInvite.md) | Yes|
|new\_invite|[ExportedChatInvite](/API_docs/types/ExportedChatInvite.md) | Yes|



### Type: [ChannelAdminLogEventAction](/API_docs/types/ChannelAdminLogEventAction.md)


### Example:

```php
$channelAdminLogEventActionExportedInviteEdit = ['_' => 'channelAdminLogEventActionExportedInviteEdit', 'prev_invite' => ExportedChatInvite, 'new_invite' => ExportedChatInvite];
```  
