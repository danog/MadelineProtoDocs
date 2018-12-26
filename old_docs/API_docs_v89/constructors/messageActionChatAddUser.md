---
title: messageActionChatAddUser
description: Message action chat add user
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageActionChatAddUser  
[Back to constructors index](index.md)



Message action chat add user

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|users|Array of [int](../types/int.md) | Yes|Users|



### Type: [MessageAction](../types/MessageAction.md)


### Example:

```php
$messageActionChatAddUser = ['_' => 'messageActionChatAddUser', 'users' => [int, int]];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "messageActionChatAddUser", "users": [int]}
```


Or, if you're into Lua:

```lua
messageActionChatAddUser={_='messageActionChatAddUser', users={int}}

```


