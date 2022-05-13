---
title: "channels.channelParticipants"
description: "Represents multiple channel participants"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/channels_channelParticipants.html
---
# Constructor: channels.channelParticipants  
[Back to constructors index](/API_docs/constructors/index.html)



Represents multiple channel participants

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|count|[int](/API_docs/types/int.html) | Yes|Total number of participants that correspond to the given query|
|participants|Array of [ChannelParticipant](/API_docs/types/ChannelParticipant.html) | Yes|Participants|
|chats|Array of [Chat](/API_docs/types/Chat.html) | Yes|Mentioned chats|
|users|Array of [User](/API_docs/types/User.html) | Yes|Users mentioned in participant info|



### Type: [channels.ChannelParticipants](/API_docs/types/channels.ChannelParticipants.html)


### Example:

```
$channels_channelParticipants = ['_' => 'channels.channelParticipants', 'count' => int, 'participants' => [ChannelParticipant, ChannelParticipant], 'chats' => [Chat, Chat], 'users' => [User, User]];
```  
