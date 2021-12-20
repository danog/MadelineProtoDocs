---
title: "securePlainPhone"
description: "Phone number to use in telegram passport: it must be verified, first »."
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: securePlainPhone  
[Back to constructors index](index.md)



Phone number to use in [telegram passport](https://core.telegram.org/passport): [it must be verified, first »](https://core.telegram.org/passport/encryption#secureplaindata).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|phone|[string](../types/string.md) | Yes|Phone number|



### Type: [SecurePlainData](../types/SecurePlainData.md)


### Example:

```php
$securePlainPhone = ['_' => 'securePlainPhone', 'phone' => 'string'];
```  


Or, if you're into Lua:

```lua
securePlainPhone={_='securePlainPhone', phone='string'}

```


