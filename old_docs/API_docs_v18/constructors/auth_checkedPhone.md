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
|phone\_invited|[Bool](../types/Bool.md) | Yes|Phone invited?|



### Type: [auth\_CheckedPhone](../types/auth_CheckedPhone.md)


### Example:

```php
$auth_checkedPhone = ['_' => 'auth.checkedPhone', 'phone_registered' => Bool, 'phone_invited' => Bool];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "auth.checkedPhone", "phone_registered": Bool, "phone_invited": Bool}
```


Or, if you're into Lua:

```lua
auth_checkedPhone={_='auth.checkedPhone', phone_registered=Bool, phone_invited=Bool}

```


