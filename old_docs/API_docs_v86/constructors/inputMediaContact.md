---
title: inputMediaContact
description: Media contact
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputMediaContact  
[Back to constructors index](index.md)



Media contact

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|phone\_number|[string](../types/string.md) | Yes|Phone number|
|first\_name|[string](../types/string.md) | Yes|First name|
|last\_name|[string](../types/string.md) | Yes|Last name|
|vcard|[string](../types/string.md) | Yes|Vcard|



### Type: [InputMedia](../types/InputMedia.md)


### Example:

```php
$inputMediaContact = ['_' => 'inputMediaContact', 'phone_number' => 'string', 'first_name' => 'string', 'last_name' => 'string', 'vcard' => 'string'];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "inputMediaContact", "phone_number": "string", "first_name": "string", "last_name": "string", "vcard": "string"}
```


Or, if you're into Lua:

```lua
inputMediaContact={_='inputMediaContact', phone_number='string', first_name='string', last_name='string', vcard='string'}

```


