---
title: messageActionChatAddUser
description: New member in the group
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageActionChatAddUser  
[Back to constructors index](index.md)



New member in the group

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|users|Array of [long](../types/long.md) | Yes|Users that were invited to the chat|



### Type: [MessageAction](../types/MessageAction.md)


### Example:

```php
$messageActionChatAddUser = ['_' => 'messageActionChatAddUser', 'users' => [long, long]];
```  


Or, if you're into Lua:

```lua
messageActionChatAddUser={_='messageActionChatAddUser', users={long}}

```


