---
title: recentMeUrlChatInvite
description: Recent me URL chat invite
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: recentMeUrlChatInvite  
[Back to constructors index](index.md)



Recent me URL chat invite

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|url|[string](../types/string.md) | Yes|URL|
|chat\_invite|[ChatInvite](../types/ChatInvite.md) | Optional|Chat invite|



### Type: [RecentMeUrl](../types/RecentMeUrl.md)


### Example:

```php
$recentMeUrlChatInvite = ['_' => 'recentMeUrlChatInvite', 'url' => 'string', 'chat_invite' => ChatInvite];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "recentMeUrlChatInvite", "url": "string", "chat_invite": ChatInvite}
```


Or, if you're into Lua:

```lua
recentMeUrlChatInvite={_='recentMeUrlChatInvite', url='string', chat_invite=ChatInvite}

```


