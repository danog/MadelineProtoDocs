---
title: messageActionChatAddUser
description: messageActionChatAddUser attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
## Constructor: messageActionChatAddUser  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|users|Array of [int](../types/int.md) | Yes|



### Type: [MessageAction](../types/MessageAction.md)


### Example:

```
$messageActionChatAddUser = ['_' => 'messageActionChatAddUser', 'users' => [int, int]];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "messageActionChatAddUser", "users": [int]}
```


Or, if you're into Lua:  


```
messageActionChatAddUser={_='messageActionChatAddUser', users={int}}

```


