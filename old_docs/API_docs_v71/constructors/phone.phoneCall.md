---
title: phone.phoneCall
description: A VoIP phone call
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: phone.phoneCall  
[Back to constructors index](index.md)



A VoIP phone call

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|phone\_call|[PhoneCall](../types/PhoneCall.md) | Optional|The VoIP phone call|
|users|Array of [User](../types/User.md) | Yes|Users|



### Type: [phone.PhoneCall](../types/phone.PhoneCall.md)


### Example:

```php
$phone.phoneCall = ['_' => 'phone.phoneCall', 'phone_call' => PhoneCall, 'users' => [User, User]];
```  


Or, if you're into Lua:

```lua
phone.phoneCall={_='phone.phoneCall', phone_call=PhoneCall, users={User}}

```


