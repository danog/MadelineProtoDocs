# channels.channelParticipant

> Represents a channel participant

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
