---
title: "channels.channelParticipant"
description: "Represents a channel participant"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/channels_channelParticipant.html
---
# Constructor: channels.channelParticipant  
[Back to constructors index](/API_docs/constructors/index.md)



Represents a channel participant

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|participant|[ChannelParticipant](/API_docs/types/ChannelParticipant.md) | Yes|The channel participant|
|chats|Array of [Chat](/API_docs/types/Chat.md) | Yes|
|users|Array of [User](/API_docs/types/User.md) | Yes|Users|



### Type: [channels.ChannelParticipant](/API_docs/types/channels.ChannelParticipant.md)


### Example:

```php
$channels_channelParticipant = ['_' => 'channels.channelParticipant', 'participant' => ChannelParticipant, 'chats' => [Chat, Chat], 'users' => [User, User]];
```  
