---
title: "dcOption"
description: "Data centre"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: dcOption  
[Back to constructors index](/API_docs/constructors/index.md)



Data centre

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|ipv6|[Bool](/API_docs/types/Bool.md) | Optional|Whether the specified IP is an IPv6 address|
|media\_only|[Bool](/API_docs/types/Bool.md) | Optional|Whether this DC should only be used to [download or upload files](https://core.telegram.org/api/files)|
|tcpo\_only|[Bool](/API_docs/types/Bool.md) | Optional|Whether this DC only supports connection with [transport obfuscation](https://core.telegram.org/mtproto/mtproto-transports#transport-obfuscation)|
|cdn|[Bool](/API_docs/types/Bool.md) | Optional|Whether this is a [CDN DC](https://core.telegram.org/cdn).|
|static|[Bool](/API_docs/types/Bool.md) | Optional|If set, this IP should be used when connecting through a proxy|
|id|[int](/API_docs/types/int.md) | Yes|DC ID|
|ip\_address|[string](/API_docs/types/string.md) | Yes|IP address of DC|
|port|[int](/API_docs/types/int.md) | Yes|Port|
|secret|[bytes](/API_docs/types/bytes.md) | Optional|If the `tcpo_only` flag is set, specifies the secret to use when connecting using [transport obfuscation](https://core.telegram.org/mtproto/mtproto-transports#transport-obfuscation)|



### Type: [DcOption](/API_docs/types/DcOption.md)


### Example:

```php
$dcOption = ['_' => 'dcOption', 'ipv6' => Bool, 'media_only' => Bool, 'tcpo_only' => Bool, 'cdn' => Bool, 'static' => Bool, 'id' => int, 'ip_address' => 'string', 'port' => int, 'secret' => 'bytes'];
```  
