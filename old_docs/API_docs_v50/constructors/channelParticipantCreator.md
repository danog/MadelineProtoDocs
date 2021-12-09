---
title: channelParticipantCreator
description: Channel/supergroup creator
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: channelParticipantCreator  
[Back to constructors index](index.md)



Channel/supergroup creator

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|user\_id|[long](../types/long.md) | Yes|
|admin\_rights|[ChatAdminRights](../types/ChatAdminRights.md) | Yes|Creator admin rights|
|rank|[string](../types/string.md) | Optional|The role (rank) of the group creator in the group: just an arbitrary string, `admin` by default|



### Type: [ChannelParticipant](../types/ChannelParticipant.md)


### Example:

```php
$channelParticipantCreator = ['_' => 'channelParticipantCreator', 'user_id' => long, 'admin_rights' => ChatAdminRights, 'rank' => 'string'];
```  


Or, if you're into Lua:

```lua
channelParticipantCreator={_='channelParticipantCreator', user_id=long, admin_rights=ChatAdminRights, rank='string'}

```


