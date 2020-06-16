---
title: recentMeUrlChat
description: Recent t.me link to a chat
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: recentMeUrlChat  
[Back to constructors index](index.md)



Recent t.me link to a chat

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|url|[string](../types/string.md) | Yes|t.me URL|
|chat\_id|[int](../types/int.md) | Yes|Chat ID|



### Type: [RecentMeUrl](../types/RecentMeUrl.md)


### Example:

```php
$recentMeUrlChat = ['_' => 'recentMeUrlChat', 'url' => 'string', 'chat_id' => int];
```  


Or, if you're into Lua:

```lua
recentMeUrlChat={_='recentMeUrlChat', url='string', chat_id=int}

```


