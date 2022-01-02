---
title: "recentMeUrlChatInvite"
description: "Recent t.me invite link to a chat"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: recentMeUrlChatInvite  
[Back to constructors index](index.md)



Recent t.me invite link to a chat

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|url|[string](../types/string.md) | Yes|t.me URL|
|chat\_invite|[ChatInvite](../types/ChatInvite.md) | Yes|Chat invitation|



### Type: [RecentMeUrl](../types/RecentMeUrl.md)


### Example:

```php
$recentMeUrlChatInvite = ['_' => 'recentMeUrlChatInvite', 'url' => 'string', 'chat_invite' => ChatInvite];
```  


Or, if you're into Lua:

```lua
recentMeUrlChatInvite={_='recentMeUrlChatInvite', url='string', chat_invite=ChatInvite}

```


