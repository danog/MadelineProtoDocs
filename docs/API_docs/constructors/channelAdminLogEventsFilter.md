---
title: "channelAdminLogEventsFilter"
description: "Filter only certain admin log events"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: channelAdminLogEventsFilter  
[Back to constructors index](/API_docs/constructors/index.html)



Filter only certain admin log events

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|join|[Bool](/API_docs/types/Bool.html) | Optional|[Join events](../constructors/channelAdminLogEventActionParticipantJoin.html)|
|leave|[Bool](/API_docs/types/Bool.html) | Optional|[Leave events](../constructors/channelAdminLogEventActionParticipantLeave.html)|
|invite|[Bool](/API_docs/types/Bool.html) | Optional|[Invite events](../constructors/channelAdminLogEventActionParticipantInvite.html)|
|ban|[Bool](/API_docs/types/Bool.html) | Optional|[Ban events](../constructors/channelAdminLogEventActionParticipantToggleBan.html)|
|unban|[Bool](/API_docs/types/Bool.html) | Optional|[Unban events](../constructors/channelAdminLogEventActionParticipantToggleBan.html)|
|kick|[Bool](/API_docs/types/Bool.html) | Optional|[Kick events](../constructors/channelAdminLogEventActionParticipantToggleBan.html)|
|unkick|[Bool](/API_docs/types/Bool.html) | Optional|[Unkick events](../constructors/channelAdminLogEventActionParticipantToggleBan.html)|
|promote|[Bool](/API_docs/types/Bool.html) | Optional|[Admin promotion events](../constructors/channelAdminLogEventActionParticipantToggleAdmin.html)|
|demote|[Bool](/API_docs/types/Bool.html) | Optional|[Admin demotion events](../constructors/channelAdminLogEventActionParticipantToggleAdmin.html)|
|info|[Bool](/API_docs/types/Bool.html) | Optional|Info change events (when [about](../constructors/channelAdminLogEventActionChangeAbout.html), [linked chat](../constructors/channelAdminLogEventActionChangeLinkedChat.html), [location](../constructors/channelAdminLogEventActionChangeLocation.html), [photo](../constructors/channelAdminLogEventActionChangePhoto.html), [stickerset](../constructors/channelAdminLogEventActionChangeStickerSet.html), [title](../constructors/channelAdminLogEventActionChangeTitle.html) or [username](../constructors/channelAdminLogEventActionChangeUsername.html) data of a channel gets modified)|
|settings|[Bool](/API_docs/types/Bool.html) | Optional|Settings change events ([invites](../constructors/channelAdminLogEventActionToggleInvites.html), [hidden prehistory](../constructors/channelAdminLogEventActionTogglePreHistoryHidden.html), [signatures](../constructors/channelAdminLogEventActionToggleSignatures.html), [default banned rights](../constructors/channelAdminLogEventActionDefaultBannedRights.html))|
|pinned|[Bool](/API_docs/types/Bool.html) | Optional|[Message pin events](../constructors/channelAdminLogEventActionUpdatePinned.html)|
|edit|[Bool](/API_docs/types/Bool.html) | Optional|[Message edit events](../constructors/channelAdminLogEventActionEditMessage.html)|
|delete|[Bool](/API_docs/types/Bool.html) | Optional|[Message deletion events](../constructors/channelAdminLogEventActionDeleteMessage.html)|
|group\_call|[Bool](/API_docs/types/Bool.html) | Optional|Group call events|
|invites|[Bool](/API_docs/types/Bool.html) | Optional|Invite events|
|send|[Bool](/API_docs/types/Bool.html) | Optional|A message was posted in a channel|



### Type: [ChannelAdminLogEventsFilter](/API_docs/types/ChannelAdminLogEventsFilter.html)


### Example:

```
$channelAdminLogEventsFilter = ['_' => 'channelAdminLogEventsFilter', 'join' => Bool, 'leave' => Bool, 'invite' => Bool, 'ban' => Bool, 'unban' => Bool, 'kick' => Bool, 'unkick' => Bool, 'promote' => Bool, 'demote' => Bool, 'info' => Bool, 'settings' => Bool, 'pinned' => Bool, 'edit' => Bool, 'delete' => Bool, 'group_call' => Bool, 'invites' => Bool, 'send' => Bool];
```  
