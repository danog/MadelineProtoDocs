---
title: channels.channelParticipant
description: Represents a channel participant
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: channels.channelParticipant  
[Back to constructors index](index.md)



Represents a channel participant

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|participant|[ChannelParticipant](../types/ChannelParticipant.md) | Yes|The channel participant|
|users|Array of [User](../types/User.md) | Yes|Users|



### Type: [channels.ChannelParticipant](../types/channels.ChannelParticipant.md)


### Example:

```php
$channels.channelParticipant = ['_' => 'channels.channelParticipant', 'participant' => ChannelParticipant, 'users' => [User, User]];
```  


Or, if you're into Lua:

```lua
channels.channelParticipant={_='channels.channelParticipant', participant=ChannelParticipant, users={User}}

```


