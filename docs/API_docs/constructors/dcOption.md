---
title: "dcOption"
description: "Data centre"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: dcOption  
[Back to constructors index](index.md)



Data centre

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|ipv6|[Bool](../types/Bool.md) | Optional|Whether the specified IP is an IPv6 address|
|media\_only|[Bool](../types/Bool.md) | Optional|Whether this DC should only be used to [download or upload files](https://core.telegram.org/api/files)|
|tcpo\_only|[Bool](../types/Bool.md) | Optional|Whether this DC only supports connection with [transport obfuscation](https://core.telegram.org/mtproto/mtproto-transports#transport-obfuscation)|
|cdn|[Bool](../types/Bool.md) | Optional|Whether this is a [CDN DC](https://core.telegram.org/cdn).|
|static|[Bool](../types/Bool.md) | Optional|If set, this IP should be used when connecting through a proxy|
|id|[int](../types/int.md) | Yes|DC ID|
|ip\_address|[string](../types/string.md) | Yes|IP address of DC|
|port|[int](../types/int.md) | Yes|Port|
|secret|[bytes](../types/bytes.md) | Optional|If the `tcpo_only` flag is set, specifies the secret to use when connecting using [transport obfuscation](https://core.telegram.org/mtproto/mtproto-transports#transport-obfuscation)|



### Type: [DcOption](../types/DcOption.md)


### Example:

```php
$dcOption = ['_' => 'dcOption', 'ipv6' => Bool, 'media_only' => Bool, 'tcpo_only' => Bool, 'cdn' => Bool, 'static' => Bool, 'id' => int, 'ip_address' => 'string', 'port' => int, 'secret' => 'bytes'];
```  


Or, if you're into Lua:

```lua
dcOption={_='dcOption', ipv6=Bool, media_only=Bool, tcpo_only=Bool, cdn=Bool, static=Bool, id=int, ip_address='string', port=int, secret='bytes'}

```


