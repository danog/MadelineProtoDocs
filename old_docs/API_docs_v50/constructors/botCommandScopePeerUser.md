---
title: botCommandScopePeerUser
description: botCommandScopePeerUser attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: botCommandScopePeerUser  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|peer|[InputPeer](../types/InputPeer.md) | Optional|
|user\_id|[InputUser](../types/InputUser.md) | Optional|



### Type: [BotCommandScope](../types/BotCommandScope.md)


### Example:

```php
$botCommandScopePeerUser = ['_' => 'botCommandScopePeerUser', 'peer' => InputPeer, 'user_id' => InputUser];
```  


Or, if you're into Lua:

```lua
botCommandScopePeerUser={_='botCommandScopePeerUser', peer=InputPeer, user_id=InputUser}

```


