---
title: decryptedMessageMediaContact
description: Contact attached to an encrypted message.
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: decryptedMessageMediaContact\_8  
[Back to constructors index](index.md)



Contact attached to an encrypted message.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|phone\_number|[string](../types/string.md) | Yes|Phone number|
|first\_name|[string](../types/string.md) | Yes|Contact's first name|
|last\_name|[string](../types/string.md) | Yes|Contact's last name|
|user\_id|[int](../types/int.md) | Yes|Telegram User ID of signed-up contact|



### Type: [DecryptedMessageMedia](../types/DecryptedMessageMedia.md)


### Example:

```php
$decryptedMessageMediaContact_8 = ['_' => 'decryptedMessageMediaContact', 'phone_number' => 'string', 'first_name' => 'string', 'last_name' => 'string', 'user_id' => int];
```  


Or, if you're into Lua:

```lua
decryptedMessageMediaContact_8={_='decryptedMessageMediaContact', phone_number='string', first_name='string', last_name='string', user_id=int}

```


