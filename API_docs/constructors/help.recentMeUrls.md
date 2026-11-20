# help.recentMeUrls

> Recent t.me URLs

[Back to constructors index](/API_docs/constructors/index.html)



Recent t.me URLs

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|urls|Array of [RecentMeUrl](/API_docs/types/RecentMeUrl.html) | Yes|URLs|
|chats|Array of [Chat](/API_docs/types/Chat.html) | Yes|Chats|
|users|Array of [User](/API_docs/types/User.html) | Yes|Users|



### Type: [help.RecentMeUrls](/API_docs/types/help.RecentMeUrls.html)


### Example:

```
$help_recentMeUrls = ['_' => 'help.recentMeUrls', 'urls' => [RecentMeUrl, RecentMeUrl], 'chats' => [Chat, Chat], 'users' => [User, User]];
```
