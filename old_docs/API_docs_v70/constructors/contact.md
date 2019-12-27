---
title: contact
description: A contact of the current user that is registered in the system.
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: contact  
[Back to constructors index](index.md)



A contact of the current user that is registered in the system.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|user\_id|[int](../types/int.md) | Yes|User identifier|
|mutual|[Bool](../types/Bool.md) | Yes|Current user is in the user's contact list|



### Type: [Contact](../types/Contact.md)


### Example:

```php
$contact = ['_' => 'contact', 'user_id' => int, 'mutual' => Bool];
```  


Or, if you're into Lua:

```lua
contact={_='contact', user_id=int, mutual=Bool}

```


