---
title: auth.sentCodeTypeFlashCall
description: The code will be sent via a flash phone call, that will be closed immediately. The phone code will then be the phone number itself, just make sure that the phone number matches the specified pattern.
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: auth.sentCodeTypeFlashCall  
[Back to constructors index](index.md)



The code will be sent via a flash phone call, that will be closed immediately. The phone code will then be the phone number itself, just make sure that the phone number matches the specified pattern.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|pattern|[string](../types/string.md) | Yes|[pattern](https://core.telegram.org/api/pattern) to match|



### Type: [auth\_SentCodeType](../types/auth_SentCodeType.md)


### Example:

```php
$auth_sentCodeTypeFlashCall = ['_' => 'auth.sentCodeTypeFlashCall', 'pattern' => 'string'];
```  


Or, if you're into Lua:

```lua
auth_sentCodeTypeFlashCall={_='auth.sentCodeTypeFlashCall', pattern='string'}

```


