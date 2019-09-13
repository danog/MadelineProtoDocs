---
title: updateUserName
description: Update user name
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateUserName  
[Back to constructors index](index.md)



Update user name

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|user\_id|[int](../types/int.md) | Yes|User ID|
|first\_name|[string](../types/string.md) | Yes|First name|
|last\_name|[string](../types/string.md) | Yes|Last name|
|username|[string](../types/string.md) | Yes|Username|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateUserName = ['_' => 'updateUserName', 'user_id' => int, 'first_name' => 'string', 'last_name' => 'string', 'username' => 'string'];
```  


Or, if you're into Lua:

```lua
updateUserName={_='updateUserName', user_id=int, first_name='string', last_name='string', username='string'}

```


