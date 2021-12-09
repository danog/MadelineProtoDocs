---
title: channels.channelParticipants
description: Represents multiple channel participants
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/channels_channelParticipants.html
---
# Constructor: channels.channelParticipants  
[Back to constructors index](index.md)



Represents multiple channel participants

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|count|[int](../types/int.md) | Yes|Total number of participants that correspond to the given query|
|participants|Array of [ChannelParticipant](../types/ChannelParticipant.md) | Yes|Participants|
|chats|Array of [Chat](../types/Chat.md) | Yes|
|users|Array of [User](../types/User.md) | Yes|Users mentioned in participant info|



### Type: [channels.ChannelParticipants](../types/channels.ChannelParticipants.md)


### Example:

```php
$channels_channelParticipants = ['_' => 'channels.channelParticipants', 'count' => int, 'participants' => [ChannelParticipant, ChannelParticipant], 'chats' => [Chat, Chat], 'users' => [User, User]];
```  


Or, if you're into Lua:

```lua
channels_channelParticipants={_='channels.channelParticipants', count=int, participants={ChannelParticipant}, chats={Chat}, users={User}}

```


