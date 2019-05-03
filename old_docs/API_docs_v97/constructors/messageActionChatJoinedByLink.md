---
title: messageActionChatJoinedByLink
description: Message action chat joined by link
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageActionChatJoinedByLink  
[Back to constructors index](index.md)



Message action chat joined by link

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|inviter\_id|[int](../types/int.md) | Yes|Inviter ID|



### Type: [MessageAction](../types/MessageAction.md)


### Example:

```php
$messageActionChatJoinedByLink = ['_' => 'messageActionChatJoinedByLink', 'inviter_id' => int];
```  


Or, if you're into Lua:

```lua
messageActionChatJoinedByLink={_='messageActionChatJoinedByLink', inviter_id=int}

```


