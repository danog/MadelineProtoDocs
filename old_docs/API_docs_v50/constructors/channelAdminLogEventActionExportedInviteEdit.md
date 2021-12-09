---
title: channelAdminLogEventActionExportedInviteEdit
description: channelAdminLogEventActionExportedInviteEdit attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: channelAdminLogEventActionExportedInviteEdit  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|prev\_invite|[ExportedChatInvite](../types/ExportedChatInvite.md) | Yes|
|new\_invite|[ExportedChatInvite](../types/ExportedChatInvite.md) | Yes|



### Type: [ChannelAdminLogEventAction](../types/ChannelAdminLogEventAction.md)


### Example:

```php
$channelAdminLogEventActionExportedInviteEdit = ['_' => 'channelAdminLogEventActionExportedInviteEdit', 'prev_invite' => ExportedChatInvite, 'new_invite' => ExportedChatInvite];
```  


Or, if you're into Lua:

```lua
channelAdminLogEventActionExportedInviteEdit={_='channelAdminLogEventActionExportedInviteEdit', prev_invite=ExportedChatInvite, new_invite=ExportedChatInvite}

```


