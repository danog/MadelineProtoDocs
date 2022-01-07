---
title: "channelAdminLogEventActionExportedInviteEdit"
description: "channelAdminLogEventActionExportedInviteEdit attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: channelAdminLogEventActionExportedInviteEdit  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|prev\_invite|[ExportedChatInvite](/API_docs/types/ExportedChatInvite.html) | Yes|
|new\_invite|[ExportedChatInvite](/API_docs/types/ExportedChatInvite.html) | Yes|



### Type: [ChannelAdminLogEventAction](/API_docs/types/ChannelAdminLogEventAction.html)


### Example:

```php
$channelAdminLogEventActionExportedInviteEdit = ['_' => 'channelAdminLogEventActionExportedInviteEdit', 'prev_invite' => ExportedChatInvite, 'new_invite' => ExportedChatInvite];
```  
