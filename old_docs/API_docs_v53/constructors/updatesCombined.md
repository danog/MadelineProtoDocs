---
title: updatesCombined
description: Updates combined
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updatesCombined  
[Back to constructors index](index.md)



Updates combined

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|updates|Array of [Update](../types/Update.md) | Yes|Updates|
|users|Array of [User](../types/User.md) | Yes|Users|
|chats|Array of [Chat](../types/Chat.md) | Yes|Chats|
|date|[int](../types/int.md) | Yes|Date|
|seq\_start|[int](../types/int.md) | Yes|Seq start|
|seq|[int](../types/int.md) | Yes|Seq|



### Type: [Updates](../types/Updates.md)


### Example:

```php
$updatesCombined = ['_' => 'updatesCombined', 'updates' => [Update, Update], 'users' => [User, User], 'chats' => [Chat, Chat], 'date' => int, 'seq_start' => int, 'seq' => int];
```  


Or, if you're into Lua:

```lua
updatesCombined={_='updatesCombined', updates={Update}, users={User}, chats={Chat}, date=int, seq_start=int, seq=int}

```


