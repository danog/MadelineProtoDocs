---
title: updates
description: Updates
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updates  
[Back to constructors index](index.md)



Updates

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|updates|Array of [Update](../types/Update.md) | Yes|Updates|
|users|Array of [User](../types/User.md) | Yes|Users|
|chats|Array of [Chat](../types/Chat.md) | Yes|Chats|
|date|[int](../types/int.md) | Yes|Date|
|seq|[int](../types/int.md) | Yes|Seq|



### Type: [Updates](../types/Updates.md)


### Example:

```php
$updates = ['_' => 'updates', 'updates' => [Update, Update], 'users' => [User, User], 'chats' => [Chat, Chat], 'date' => int, 'seq' => int];
```  


Or, if you're into Lua:

```lua
updates={_='updates', updates={Update}, users={User}, chats={Chat}, date=int, seq=int}

```


