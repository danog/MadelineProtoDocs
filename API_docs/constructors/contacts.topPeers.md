# contacts.topPeers

> Top peers

[Back to constructors index](/API_docs/constructors/index.html)



Top peers

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|categories|Array of [TopPeerCategoryPeers](/API_docs/types/TopPeerCategoryPeers.html) | Yes|Top peers by top peer category|
|chats|Array of [Chat](/API_docs/types/Chat.html) | Yes|Chats|
|users|Array of [User](/API_docs/types/User.html) | Yes|Users|



### Type: [contacts.TopPeers](/API_docs/types/contacts.TopPeers.html)


### Example:

```
$contacts_topPeers = ['_' => 'contacts.topPeers', 'categories' => [TopPeerCategoryPeers, TopPeerCategoryPeers], 'chats' => [Chat, Chat], 'users' => [User, User]];
```
