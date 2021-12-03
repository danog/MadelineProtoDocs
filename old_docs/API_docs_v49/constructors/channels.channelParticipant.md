---
title: channels.channelParticipant
description: Represents a channel participant
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/channels_channelParticipant.html
---
# Constructor: channels.channelParticipant  
[Back to constructors index](index.md)



Represents a channel participant

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|participant|[ChannelParticipant](../types/ChannelParticipant.md) | Yes|The channel participant|
|chats|Array of [Chat](../types/Chat.md) | Yes|
|users|Array of [User](../types/User.md) | Yes|Users|



### Type: [channels.ChannelParticipant](../types/channels.ChannelParticipant.md)


### Example:

```php
$channels_channelParticipant = ['_' => 'channels.channelParticipant', 'participant' => ChannelParticipant, 'chats' => [Chat, Chat], 'users' => [User, User]];
```  


Or, if you're into Lua:

```lua
channels_channelParticipant={_='channels.channelParticipant', participant=ChannelParticipant, chats={Chat}, users={User}}

```


