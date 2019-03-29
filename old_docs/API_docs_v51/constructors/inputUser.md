---
title: inputUser
description: User
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputUser  
[Back to constructors index](index.md)



User

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|user\_id|[int](../types/int.md) | Yes|User ID|
|access\_hash|[long](../types/long.md) | Yes|Access hash|



### Type: [InputUser](../types/InputUser.md)


### Example:

```php
$inputUser = ['_' => 'inputUser', 'user_id' => int, 'access_hash' => long];
```  


Or, if you're into Lua:

```lua
inputUser={_='inputUser', user_id=int, access_hash=long}

```


