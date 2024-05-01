---
title: "recentMeUrlChatInvite"
description: "Recent t.me invite link to a chat"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: recentMeUrlChatInvite  
[Back to constructors index](/API_docs/constructors/index.html)



Recent t.me invite link to a chat

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|url|[string](/API_docs/types/string.html) | Yes|t.me URL|
|chat\_invite|[ChatInvite](/API_docs/types/ChatInvite.html) | Yes|Chat invitation|



### Type: [RecentMeUrl](/API_docs/types/RecentMeUrl.html)


### Example:

```
$recentMeUrlChatInvite = ['_' => 'recentMeUrlChatInvite', 'url' => 'string', 'chat_invite' => ChatInvite];
```  
