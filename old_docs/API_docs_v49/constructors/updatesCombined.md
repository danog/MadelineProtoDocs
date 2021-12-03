---
title: updatesCombined
description: Constructor for a group of updates.
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updatesCombined  
[Back to constructors index](index.md)



Constructor for a group of updates.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|updates|Array of [Update](../types/Update.md) | Yes|List of updates|
|users|Array of [User](../types/User.md) | Yes|List of users mentioned in updates|
|chats|Array of [Chat](../types/Chat.md) | Yes|List of chats mentioned in updates|
|date|[int](../types/int.md) | Yes|Current date|
|seq\_start|[int](../types/int.md) | Yes|Value **seq** for the earliest update in a group|
|seq|[int](../types/int.md) | Yes|Value **seq** for the latest update in a group|



### Type: [Updates](../types/Updates.md)


### Example:

```php
$updatesCombined = ['_' => 'updatesCombined', 'updates' => [Update, Update], 'users' => [User, User], 'chats' => [Chat, Chat], 'date' => int, 'seq_start' => int, 'seq' => int];
```  


Or, if you're into Lua:

```lua
updatesCombined={_='updatesCombined', updates={Update}, users={User}, chats={Chat}, date=int, seq_start=int, seq=int}

```


