---
title: messageActionChatCreate
description: Message action chat create
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageActionChatCreate  
[Back to constructors index](index.md)



Message action chat create

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|title|[string](../types/string.md) | Yes|Title|
|users|Array of [int](../types/int.md) | Yes|Users|



### Type: [MessageAction](../types/MessageAction.md)


### Example:

```php
$messageActionChatCreate = ['_' => 'messageActionChatCreate', 'title' => 'string', 'users' => [int, int]];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "messageActionChatCreate", "title": "string", "users": [int]}
```


Or, if you're into Lua:

```lua
messageActionChatCreate={_='messageActionChatCreate', title='string', users={int}}

```


