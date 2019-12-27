---
title: messageActionChatJoinedByLink
description: A user joined the chat via an invite link
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageActionChatJoinedByLink  
[Back to constructors index](index.md)



A user joined the chat via an invite link

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|inviter\_id|[int](../types/int.md) | Yes|ID of the user that created the invite link|



### Type: [MessageAction](../types/MessageAction.md)


### Example:

```php
$messageActionChatJoinedByLink = ['_' => 'messageActionChatJoinedByLink', 'inviter_id' => int];
```  


Or, if you're into Lua:

```lua
messageActionChatJoinedByLink={_='messageActionChatJoinedByLink', inviter_id=int}

```


