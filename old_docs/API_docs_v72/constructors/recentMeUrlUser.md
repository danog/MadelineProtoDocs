---
title: recentMeUrlUser
description: Recent me URL user
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: recentMeUrlUser  
[Back to constructors index](index.md)



Recent me URL user

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|url|[string](../types/string.md) | Yes|URL|
|user\_id|[int](../types/int.md) | Yes|User ID|



### Type: [RecentMeUrl](../types/RecentMeUrl.md)


### Example:

```php
$recentMeUrlUser = ['_' => 'recentMeUrlUser', 'url' => 'string', 'user_id' => int];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "recentMeUrlUser", "url": "string", "user_id": int}
```


Or, if you're into Lua:

```lua
recentMeUrlUser={_='recentMeUrlUser', url='string', user_id=int}

```


