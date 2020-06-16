---
title: auth.checkedPhone
description: auth.checkedPhone attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/auth_checkedPhone.html
---
# Constructor: auth.checkedPhone  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|phone\_registered|[Bool](../types/Bool.md) | Yes|
|phone\_invited|[Bool](../types/Bool.md) | Yes|



### Type: [auth.CheckedPhone](../types/auth.CheckedPhone.md)


### Example:

```php
$auth.checkedPhone = ['_' => 'auth.checkedPhone', 'phone_registered' => Bool, 'phone_invited' => Bool];
```  


Or, if you're into Lua:

```lua
auth.checkedPhone={_='auth.checkedPhone', phone_registered=Bool, phone_invited=Bool}

```


