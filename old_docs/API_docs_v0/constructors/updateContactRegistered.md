---
title: updateContactRegistered
description: updateContactRegistered attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateContactRegistered  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|user\_id|[int](../types/int.md) | Yes|
|date|[int](../types/int.md) | Yes|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateContactRegistered = ['_' => 'updateContactRegistered', 'user_id' => int, 'date' => int];
```  


Or, if you're into Lua:

```lua
updateContactRegistered={_='updateContactRegistered', user_id=int, date=int}

```


