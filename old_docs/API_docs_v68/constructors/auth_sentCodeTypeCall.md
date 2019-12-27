---
title: auth.sentCodeTypeCall
description: The code will be sent via a phone call: a synthesized voice will tell the user which verification code to input.
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: auth.sentCodeTypeCall  
[Back to constructors index](index.md)



The code will be sent via a phone call: a synthesized voice will tell the user which verification code to input.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|length|[int](../types/int.md) | Yes|Length of the verification code|



### Type: [auth\_SentCodeType](../types/auth_SentCodeType.md)


### Example:

```php
$auth_sentCodeTypeCall = ['_' => 'auth.sentCodeTypeCall', 'length' => int];
```  


Or, if you're into Lua:

```lua
auth_sentCodeTypeCall={_='auth.sentCodeTypeCall', length=int}

```


