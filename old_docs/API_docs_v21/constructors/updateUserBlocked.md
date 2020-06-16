---
title: updateUserBlocked
description: User was added to the blacklist (method [contacts.block](../methods/contacts.block.md)) or removed from the blacklist (method [contacts.unblock](../methods/contacts.unblock.md)).
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateUserBlocked  
[Back to constructors index](index.md)



User was added to the blacklist (method [contacts.block](../methods/contacts.block.md)) or removed from the blacklist (method [contacts.unblock](../methods/contacts.unblock.md)).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|user\_id|[int](../types/int.md) | Yes|User id|
|blocked|[Bool](../types/Bool.md) | Yes|([boolTrue](../constructors/boolTrue.md)) if the the user is blocked|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateUserBlocked = ['_' => 'updateUserBlocked', 'user_id' => int, 'blocked' => Bool];
```  


Or, if you're into Lua:

```lua
updateUserBlocked={_='updateUserBlocked', user_id=int, blocked=Bool}

```


