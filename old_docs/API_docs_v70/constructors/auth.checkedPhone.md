---
title: auth.checkedPhone
description: Checked phone
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: auth.checkedPhone  
[Back to constructors index](index.md)



Checked phone

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|phone\_registered|[Bool](../types/Bool.md) | Yes|Phone registered?|



### Type: [auth.CheckedPhone](../types/auth.CheckedPhone.md)


### Example:

```php
$auth.checkedPhone = ['_' => 'auth.checkedPhone', 'phone_registered' => Bool];
```  


Or, if you're into Lua:

```lua
auth.checkedPhone={_='auth.checkedPhone', phone_registered=Bool}

```


