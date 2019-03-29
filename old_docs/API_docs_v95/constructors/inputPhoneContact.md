---
title: inputPhoneContact
description: Phone contact
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputPhoneContact  
[Back to constructors index](index.md)



Phone contact

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|client\_id|[long](../types/long.md) | Yes|Client ID|
|phone|[string](../types/string.md) | Yes|Phone|
|first\_name|[string](../types/string.md) | Yes|First name|
|last\_name|[string](../types/string.md) | Yes|Last name|



### Type: [InputContact](../types/InputContact.md)


### Example:

```php
$inputPhoneContact = ['_' => 'inputPhoneContact', 'client_id' => long, 'phone' => 'string', 'first_name' => 'string', 'last_name' => 'string'];
```  


Or, if you're into Lua:

```lua
inputPhoneContact={_='inputPhoneContact', client_id=long, phone='string', first_name='string', last_name='string'}

```


