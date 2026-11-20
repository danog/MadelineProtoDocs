# messages.exportedChatInviteReplaced

> The specified chat invite was replaced with another one

[Back to constructors index](/API_docs/constructors/index.html)



The specified chat invite was replaced with another one

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|invite|[ExportedChatInvite](/API_docs/types/ExportedChatInvite.html) | Yes|The replaced chat invite|
|new\_invite|[ExportedChatInvite](/API_docs/types/ExportedChatInvite.html) | Yes|The invite that replaces the previous invite|
|users|Array of [User](/API_docs/types/User.html) | Yes|Mentioned users|



### Type: [messages.ExportedChatInvite](/API_docs/types/messages.ExportedChatInvite.html)


### Example:

```
$messages_exportedChatInviteReplaced = ['_' => 'messages.exportedChatInviteReplaced', 'invite' => ExportedChatInvite, 'new_invite' => ExportedChatInvite, 'users' => [User, User]];
```
