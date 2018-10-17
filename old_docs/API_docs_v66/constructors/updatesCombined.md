---
title: updatesCombined
description: updatesCombined attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updatesCombined  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|updates|Array of [Update](../types/Update.md) | Yes|
|users|Array of [User](../types/User.md) | Yes|
|chats|Array of [Chat](../types/Chat.md) | Yes|
|date|[int](../types/int.md) | Yes|
|seq\_start|[int](../types/int.md) | Yes|
|seq|[int](../types/int.md) | Yes|



### Type: [Updates](../types/Updates.md)


### Example:

```php
$updatesCombined = ['_' => 'updatesCombined', 'updates' => [Update, Update], 'users' => [User, User], 'chats' => [Chat, Chat], 'date' => int, 'seq_start' => int, 'seq' => int];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "updatesCombined", "updates": [Update], "users": [User], "chats": [Chat], "date": int, "seq_start": int, "seq": int}
```


Or, if you're into Lua:

```lua
updatesCombined={_='updatesCombined', updates={Update}, users={User}, chats={Chat}, date=int, seq_start=int, seq=int}

```


