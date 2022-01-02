---
title: "phone.phoneCall"
description: "A VoIP phone call"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/phone_phoneCall.html
---
# Constructor: phone.phoneCall  
[Back to constructors index](index.md)



A VoIP phone call

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|phone\_call|[PhoneCall](../types/PhoneCall.md) | Optional|The VoIP phone call|
|users|Array of [User](../types/User.md) | Yes|VoIP phone call participants|



### Type: [phone.PhoneCall](../types/phone.PhoneCall.md)


### Example:

```php
$phone_phoneCall = ['_' => 'phone.phoneCall', 'phone_call' => PhoneCall, 'users' => [User, User]];
```  


Or, if you're into Lua:

```lua
phone_phoneCall={_='phone.phoneCall', phone_call=PhoneCall, users={User}}

```


