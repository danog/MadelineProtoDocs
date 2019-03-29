---
title: savedPhoneContact
description: Saved phone contact
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: savedPhoneContact  
[Back to constructors index](index.md)



Saved phone contact

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|phone|[string](../types/string.md) | Yes|Phone|
|first\_name|[string](../types/string.md) | Yes|First name|
|last\_name|[string](../types/string.md) | Yes|Last name|
|date|[int](../types/int.md) | Yes|Date|



### Type: [SavedContact](../types/SavedContact.md)


### Example:

```php
$savedPhoneContact = ['_' => 'savedPhoneContact', 'phone' => 'string', 'first_name' => 'string', 'last_name' => 'string', 'date' => int];
```  


Or, if you're into Lua:

```lua
savedPhoneContact={_='savedPhoneContact', phone='string', first_name='string', last_name='string', date=int}

```


