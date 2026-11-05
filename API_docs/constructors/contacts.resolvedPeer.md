# contacts.resolvedPeer

> Resolved peer

[Back to constructors index](/API_docs/constructors/index.html)



Resolved peer

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|peer|[long](/API_docs/types/long.html) | Yes|The peer|
|chats|Array of [Chat](/API_docs/types/Chat.html) | Yes|Chats|
|users|Array of [User](/API_docs/types/User.html) | Yes|Users|



### Type: [contacts.ResolvedPeer](/API_docs/types/contacts.ResolvedPeer.html)


### Example:

```
$contacts_resolvedPeer = ['_' => 'contacts.resolvedPeer', 'peer' => long, 'chats' => [Chat, Chat], 'users' => [User, User]];
```
