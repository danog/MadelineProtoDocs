---
title: contact
description: Contact
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: contact  
[Back to constructors index](index.md)



Contact

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|user\_id|[int](../types/int.md) | Yes|User ID|
|mutual|[Bool](../types/Bool.md) | Yes|Mutual?|



### Type: [Contact](../types/Contact.md)


### Example:

```php
$contact = ['_' => 'contact', 'user_id' => int, 'mutual' => Bool];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "contact", "user_id": int, "mutual": Bool}
```


Or, if you're into Lua:

```lua
contact={_='contact', user_id=int, mutual=Bool}

```


