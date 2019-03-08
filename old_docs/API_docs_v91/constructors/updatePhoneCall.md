---
title: updatePhoneCall
description: Update phone call
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updatePhoneCall  
[Back to constructors index](index.md)



Update phone call

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|phone\_call|[PhoneCall](../types/PhoneCall.md) | Optional|Phone call|



### Type: [Update](../types/Update.md)


### Example:

```php
$updatePhoneCall = ['_' => 'updatePhoneCall', 'phone_call' => PhoneCall];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "updatePhoneCall", "phone_call": PhoneCall}
```


Or, if you're into Lua:

```lua
updatePhoneCall={_='updatePhoneCall', phone_call=PhoneCall}

```


