---
title: inputMediaContact
description: Phonebook contact
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputMediaContact  
[Back to constructors index](index.md)



Phonebook contact

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|phone\_number|[string](../types/string.md) | Yes|Phone number|
|first\_name|[string](../types/string.md) | Yes|Contact's first name|
|last\_name|[string](../types/string.md) | Yes|Contact's last name|
|vcard|[string](../types/string.md) | Yes|Contact vcard|



### Type: [InputMedia](../types/InputMedia.md)


### Example:

```php
$inputMediaContact = ['_' => 'inputMediaContact', 'phone_number' => 'string', 'first_name' => 'string', 'last_name' => 'string', 'vcard' => 'string'];
```  


Or, if you're into Lua:

```lua
inputMediaContact={_='inputMediaContact', phone_number='string', first_name='string', last_name='string', vcard='string'}

```


