---
title: messageMediaContact
description: Message media contact
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageMediaContact  
[Back to constructors index](index.md)



Message media contact

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|phone\_number|[string](../types/string.md) | Yes|Phone number|
|first\_name|[string](../types/string.md) | Yes|First name|
|last\_name|[string](../types/string.md) | Yes|Last name|
|user\_id|[int](../types/int.md) | Yes|User ID|



### Type: [MessageMedia](../types/MessageMedia.md)


### Example:

```php
$messageMediaContact = ['_' => 'messageMediaContact', 'phone_number' => 'string', 'first_name' => 'string', 'last_name' => 'string', 'user_id' => int];
```  


Or, if you're into Lua:

```lua
messageMediaContact={_='messageMediaContact', phone_number='string', first_name='string', last_name='string', user_id=int}

```


