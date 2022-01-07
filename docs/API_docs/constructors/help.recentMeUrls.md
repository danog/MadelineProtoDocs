---
title: "help.recentMeUrls"
description: "Recent t.me URLs"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/help_recentMeUrls.html
---
# Constructor: help.recentMeUrls  
[Back to constructors index](/API_docs/constructors/index.md)



Recent t.me URLs

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|urls|Array of [RecentMeUrl](/API_docs/types/RecentMeUrl.md) | Yes|URLs|
|chats|Array of [Chat](/API_docs/types/Chat.md) | Yes|Chats|
|users|Array of [User](/API_docs/types/User.md) | Yes|Users|



### Type: [help.RecentMeUrls](/API_docs/types/help.RecentMeUrls.md)


### Example:

```php
$help_recentMeUrls = ['_' => 'help.recentMeUrls', 'urls' => [RecentMeUrl, RecentMeUrl], 'chats' => [Chat, Chat], 'users' => [User, User]];
```  
