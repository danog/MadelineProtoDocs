---
title: "phoneConnection"
description: "Identifies an endpoint that can be used to connect to the other user in a phone call"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: phoneConnection  
[Back to constructors index](/API_docs/constructors/index.md)



Identifies an endpoint that can be used to connect to the other user in a phone call

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[long](/API_docs/types/long.md) | Yes|Endpoint ID|
|ip|[string](/API_docs/types/string.md) | Yes|IP address of endpoint|
|ipv6|[string](/API_docs/types/string.md) | Yes|IPv6 address of endpoint|
|port|[int](/API_docs/types/int.md) | Yes|Port ID|
|peer\_tag|[bytes](/API_docs/types/bytes.md) | Yes|Our peer tag|



### Type: [PhoneConnection](/API_docs/types/PhoneConnection.md)


### Example:

```php
$phoneConnection = ['_' => 'phoneConnection', 'id' => long, 'ip' => 'string', 'ipv6' => 'string', 'port' => int, 'peer_tag' => 'bytes'];
```  
