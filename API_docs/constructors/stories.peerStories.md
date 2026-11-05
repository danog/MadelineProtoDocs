# stories.peerStories

> Active story list of a specific peer.

[Back to constructors index](/API_docs/constructors/index.html)



[Active story list](https://core.telegram.org/api/stories#watching-stories) of a specific peer.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|stories|[PeerStories](/API_docs/types/PeerStories.html) | Yes|Stories|
|chats|Array of [Chat](/API_docs/types/Chat.html) | Yes|Mentioned chats|
|users|Array of [User](/API_docs/types/User.html) | Yes|Mentioned users|



### Type: [stories.PeerStories](/API_docs/types/stories.PeerStories.html)


### Example:

```
$stories_peerStories = ['_' => 'stories.peerStories', 'stories' => PeerStories, 'chats' => [Chat, Chat], 'users' => [User, User]];
```
