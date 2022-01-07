---
title: "recentMeUrlChatInvite"
description: "Recent t.me invite link to a chat"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: recentMeUrlChatInvite  
[Back to constructors index](/API_docs/constructors/index.md)



Recent t.me invite link to a chat

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|url|[string](/API_docs/types/string.md) | Yes|t.me URL|
|chat\_invite|[ChatInvite](/API_docs/types/ChatInvite.md) | Yes|Chat invitation|



### Type: [RecentMeUrl](/API_docs/types/RecentMeUrl.md)


### Example:

```php
$recentMeUrlChatInvite = ['_' => 'recentMeUrlChatInvite', 'url' => 'string', 'chat_invite' => ChatInvite];
```  
