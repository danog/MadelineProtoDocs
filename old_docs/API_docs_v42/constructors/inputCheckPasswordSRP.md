---
title: inputCheckPasswordSRP
description: Constructor for checking the validity of a 2FA SRP password (see [SRP](https://core.telegram.org/api/srp))
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputCheckPasswordSRP  
[Back to constructors index](index.md)



Constructor for checking the validity of a 2FA SRP password (see [SRP](https://core.telegram.org/api/srp))

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|srp\_id|[long](../types/long.md) | Yes|[SRP ID](https://core.telegram.org/api/srp)|
|A|[bytes](../types/bytes.md) | Yes|`A` parameter (see [SRP](https://core.telegram.org/api/srp))|
|M1|[bytes](../types/bytes.md) | Yes|`M1` parameter (see [SRP](https://core.telegram.org/api/srp))|



### Type: [InputCheckPasswordSRP](../types/InputCheckPasswordSRP.md)


### Example:

```php
$inputCheckPasswordSRP = ['_' => 'inputCheckPasswordSRP', 'srp_id' => long, 'A' => 'bytes', 'M1' => 'bytes'];
```  


Or, if you're into Lua:

```lua
inputCheckPasswordSRP={_='inputCheckPasswordSRP', srp_id=long, A='bytes', M1='bytes'}

```


