---
title: updateContactRegistered
description: Update contact registered
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateContactRegistered  
[Back to constructors index](index.md)



Update contact registered

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|user\_id|[int](../types/int.md) | Yes|User ID|
|date|[int](../types/int.md) | Yes|Date|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateContactRegistered = ['_' => 'updateContactRegistered', 'user_id' => int, 'date' => int];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "updateContactRegistered", "user_id": int, "date": int}
```


Or, if you're into Lua:

```lua
updateContactRegistered={_='updateContactRegistered', user_id=int, date=int}

```


