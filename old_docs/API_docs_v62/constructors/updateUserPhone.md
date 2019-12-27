---
title: updateUserPhone
description: A user's phone number was changed
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateUserPhone  
[Back to constructors index](index.md)



A user's phone number was changed

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|user\_id|[int](../types/int.md) | Yes|User ID|
|phone|[string](../types/string.md) | Yes|New phone number|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateUserPhone = ['_' => 'updateUserPhone', 'user_id' => int, 'phone' => 'string'];
```  


Or, if you're into Lua:

```lua
updateUserPhone={_='updateUserPhone', user_id=int, phone='string'}

```


