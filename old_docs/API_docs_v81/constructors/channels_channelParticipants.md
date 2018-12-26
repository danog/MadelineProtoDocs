---
title: channels.channelParticipants
description: Channel participants
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: channels.channelParticipants  
[Back to constructors index](index.md)



Channel participants

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|count|[int](../types/int.md) | Yes|Count|
|participants|Array of [ChannelParticipant](../types/ChannelParticipant.md) | Yes|Participants|
|users|Array of [User](../types/User.md) | Yes|Users|



### Type: [channels\_ChannelParticipants](../types/channels_ChannelParticipants.md)


### Example:

```php
$channels_channelParticipants = ['_' => 'channels.channelParticipants', 'count' => int, 'participants' => [ChannelParticipant, ChannelParticipant], 'users' => [User, User]];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "channels.channelParticipants", "count": int, "participants": [ChannelParticipant], "users": [User]}
```


Or, if you're into Lua:

```lua
channels_channelParticipants={_='channels.channelParticipants', count=int, participants={ChannelParticipant}, users={User}}

```


