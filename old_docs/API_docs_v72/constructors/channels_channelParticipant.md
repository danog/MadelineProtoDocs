---
title: channels.channelParticipant
description: Channel participant
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: channels.channelParticipant  
[Back to constructors index](index.md)



Channel participant

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|participant|[ChannelParticipant](../types/ChannelParticipant.md) | Yes|Participant|
|users|Array of [User](../types/User.md) | Yes|Users|



### Type: [channels\_ChannelParticipant](../types/channels_ChannelParticipant.md)


### Example:

```php
$channels_channelParticipant = ['_' => 'channels.channelParticipant', 'participant' => ChannelParticipant, 'users' => [User, User]];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "channels.channelParticipant", "participant": ChannelParticipant, "users": [User]}
```


Or, if you're into Lua:

```lua
channels_channelParticipant={_='channels.channelParticipant', participant=ChannelParticipant, users={User}}

```


