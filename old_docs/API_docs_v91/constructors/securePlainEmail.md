---
title: securePlainEmail
description: Email address to use in [telegram passport](https://core.telegram.org/passport): [it must be verified, first »](https://core.telegram.org/passport/encryption#secureplaindata).
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: securePlainEmail  
[Back to constructors index](index.md)



Email address to use in [telegram passport](https://core.telegram.org/passport): [it must be verified, first »](https://core.telegram.org/passport/encryption#secureplaindata).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|email|[string](../types/string.md) | Yes|Email address|



### Type: [SecurePlainData](../types/SecurePlainData.md)


### Example:

```php
$securePlainEmail = ['_' => 'securePlainEmail', 'email' => 'string'];
```  


Or, if you're into Lua:

```lua
securePlainEmail={_='securePlainEmail', email='string'}

```


