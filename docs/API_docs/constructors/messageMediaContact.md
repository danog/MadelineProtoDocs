---
title: "messageMediaContact"
description: "Attached contact."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageMediaContact  
[Back to constructors index](index.md)



Attached contact.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|phone\_number|[string](../types/string.md) | Yes|Phone number|
|first\_name|[string](../types/string.md) | Yes|Contact's first name|
|last\_name|[string](../types/string.md) | Yes|Contact's last name|
|vcard|[string](../types/string.md) | Yes|VCARD of contact|
|user\_id|[long](../types/long.md) | Yes|



### Type: [MessageMedia](../types/MessageMedia.md)


### Example:

```php
$messageMediaContact = ['_' => 'messageMediaContact', 'phone_number' => 'string', 'first_name' => 'string', 'last_name' => 'string', 'vcard' => 'string', 'user_id' => long];
```  


Or, if you're into Lua:

```lua
messageMediaContact={_='messageMediaContact', phone_number='string', first_name='string', last_name='string', vcard='string', user_id=long}

```


