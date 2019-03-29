---
title: inputCheckPasswordSRP
description: Check password srp
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputCheckPasswordSRP  
[Back to constructors index](index.md)



Check password srp

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|srp\_id|[long](../types/long.md) | Yes|Srp ID|
|A|[bytes](../types/bytes.md) | Yes|A|
|M1|[bytes](../types/bytes.md) | Yes|M1|



### Type: [InputCheckPasswordSRP](../types/InputCheckPasswordSRP.md)


### Example:

```php
$inputCheckPasswordSRP = ['_' => 'inputCheckPasswordSRP', 'srp_id' => long, 'A' => 'bytes', 'M1' => 'bytes'];
```  


Or, if you're into Lua:

```lua
inputCheckPasswordSRP={_='inputCheckPasswordSRP', srp_id=long, A='bytes', M1='bytes'}

```


