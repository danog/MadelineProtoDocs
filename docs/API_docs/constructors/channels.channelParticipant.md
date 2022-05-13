---
title: "channels.channelParticipant"
description: "Represents a channel participant"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/channels_channelParticipant.html
---
# Constructor: channels.channelParticipant  
[Back to constructors index](/API_docs/constructors/index.html)



Represents a channel participant

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|participant|[ChannelParticipant](/API_docs/types/ChannelParticipant.html) | Yes|The channel participant|
|chats|Array of [Chat](/API_docs/types/Chat.html) | Yes|Mentioned chats|
|users|Array of [User](/API_docs/types/User.html) | Yes|Users|



### Type: [channels.ChannelParticipant](/API_docs/types/channels.ChannelParticipant.html)


### Example:

```
$channels_channelParticipant = ['_' => 'channels.channelParticipant', 'participant' => ChannelParticipant, 'chats' => [Chat, Chat], 'users' => [User, User]];
```  
