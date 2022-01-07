---
title: "channelAdminLogEventsFilter"
description: "Filter only certain admin log events"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: channelAdminLogEventsFilter  
[Back to constructors index](/API_docs/constructors/index.md)



Filter only certain admin log events

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|join|[Bool](/API_docs/types/Bool.md) | Optional|[Join events](../constructors/channelAdminLogEventActionParticipantJoin.md)|
|leave|[Bool](/API_docs/types/Bool.md) | Optional|[Leave events](../constructors/channelAdminLogEventActionParticipantLeave.md)|
|invite|[Bool](/API_docs/types/Bool.md) | Optional|[Invite events](../constructors/channelAdminLogEventActionParticipantInvite.md)|
|ban|[Bool](/API_docs/types/Bool.md) | Optional|[Ban events](../constructors/channelAdminLogEventActionParticipantToggleBan.md)|
|unban|[Bool](/API_docs/types/Bool.md) | Optional|[Unban events](../constructors/channelAdminLogEventActionParticipantToggleBan.md)|
|kick|[Bool](/API_docs/types/Bool.md) | Optional|[Kick events](../constructors/channelAdminLogEventActionParticipantToggleBan.md)|
|unkick|[Bool](/API_docs/types/Bool.md) | Optional|[Unkick events](../constructors/channelAdminLogEventActionParticipantToggleBan.md)|
|promote|[Bool](/API_docs/types/Bool.md) | Optional|[Admin promotion events](../constructors/channelAdminLogEventActionParticipantToggleAdmin.md)|
|demote|[Bool](/API_docs/types/Bool.md) | Optional|[Admin demotion events](../constructors/channelAdminLogEventActionParticipantToggleAdmin.md)|
|info|[Bool](/API_docs/types/Bool.md) | Optional|Info change events (when [about](../constructors/channelAdminLogEventActionChangeAbout.md), [linked chat](../constructors/channelAdminLogEventActionChangeLinkedChat.md), [location](../constructors/channelAdminLogEventActionChangeLocation.md), [photo](../constructors/channelAdminLogEventActionChangePhoto.md), [stickerset](../constructors/channelAdminLogEventActionChangeStickerSet.md), [title](../constructors/channelAdminLogEventActionChangeTitle.md) or [username](../constructors/channelAdminLogEventActionChangeUsername.md) data of a channel gets modified)|
|settings|[Bool](/API_docs/types/Bool.md) | Optional|Settings change events ([invites](../constructors/channelAdminLogEventActionToggleInvites.md), [hidden prehistory](../constructors/channelAdminLogEventActionTogglePreHistoryHidden.md), [signatures](../constructors/channelAdminLogEventActionToggleSignatures.md), [default banned rights](../constructors/channelAdminLogEventActionDefaultBannedRights.md))|
|pinned|[Bool](/API_docs/types/Bool.md) | Optional|[Message pin events](../constructors/channelAdminLogEventActionUpdatePinned.md)|
|edit|[Bool](/API_docs/types/Bool.md) | Optional|[Message edit events](../constructors/channelAdminLogEventActionEditMessage.md)|
|delete|[Bool](/API_docs/types/Bool.md) | Optional|[Message deletion events](../constructors/channelAdminLogEventActionDeleteMessage.md)|
|group\_call|[Bool](/API_docs/types/Bool.md) | Optional|
|invites|[Bool](/API_docs/types/Bool.md) | Optional|
|send|[Bool](/API_docs/types/Bool.md) | Optional|



### Type: [ChannelAdminLogEventsFilter](/API_docs/types/ChannelAdminLogEventsFilter.md)


### Example:

```php
$channelAdminLogEventsFilter = ['_' => 'channelAdminLogEventsFilter', 'join' => Bool, 'leave' => Bool, 'invite' => Bool, 'ban' => Bool, 'unban' => Bool, 'kick' => Bool, 'unkick' => Bool, 'promote' => Bool, 'demote' => Bool, 'info' => Bool, 'settings' => Bool, 'pinned' => Bool, 'edit' => Bool, 'delete' => Bool, 'group_call' => Bool, 'invites' => Bool, 'send' => Bool];
```  
