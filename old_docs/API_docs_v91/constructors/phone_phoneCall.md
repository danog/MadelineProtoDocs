---
title: phone.phoneCall
description: Phone call
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: phone.phoneCall  
[Back to constructors index](index.md)



Phone call

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|phone\_call|[PhoneCall](../types/PhoneCall.md) | Optional|Phone call|
|users|Array of [User](../types/User.md) | Yes|Users|



### Type: [phone\_PhoneCall](../types/phone_PhoneCall.md)


### Example:

```php
$phone_phoneCall = ['_' => 'phone.phoneCall', 'phone_call' => PhoneCall, 'users' => [User, User]];
```  


Or, if you're into Lua:

```lua
phone_phoneCall={_='phone.phoneCall', phone_call=PhoneCall, users={User}}

```


