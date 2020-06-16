---
title: inputUser
description: Defines a user for further interaction.
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputUser  
[Back to constructors index](index.md)



Defines a user for further interaction.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|user\_id|[int](../types/int.md) | Yes|User identifier|
|access\_hash|[long](../types/long.md) | Yes|**access\_hash** value from the [user](../constructors/user.md) constructor|



### Type: [InputUser](../types/InputUser.md)


### Example:

```php
$inputUser = ['_' => 'inputUser', 'user_id' => int, 'access_hash' => long];
```  


Or, if you're into Lua:

```lua
inputUser={_='inputUser', user_id=int, access_hash=long}

```


