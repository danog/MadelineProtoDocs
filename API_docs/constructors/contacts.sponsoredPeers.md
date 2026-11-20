# contacts.sponsoredPeers

> Sponsored peers.

[Back to constructors index](/API_docs/constructors/index.html)



Sponsored peers.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|peers|Array of [SponsoredPeer](/API_docs/types/SponsoredPeer.html) | Yes|Sponsored peers.|
|chats|Array of [Chat](/API_docs/types/Chat.html) | Yes|Info about sponsored chats and channels|
|users|Array of [User](/API_docs/types/User.html) | Yes|Info about sponsored users|



### Type: [contacts.SponsoredPeers](/API_docs/types/contacts.SponsoredPeers.html)


### Example:

```
$contacts_sponsoredPeers = ['_' => 'contacts.sponsoredPeers', 'peers' => [SponsoredPeer, SponsoredPeer], 'chats' => [Chat, Chat], 'users' => [User, User]];
```
