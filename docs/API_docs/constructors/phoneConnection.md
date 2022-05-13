---
title: "phoneConnection"
description: "Identifies an endpoint that can be used to connect to the other user in a phone call"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: phoneConnection  
[Back to constructors index](/API_docs/constructors/index.html)



Identifies an endpoint that can be used to connect to the other user in a phone call

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|tcp|[Bool](/API_docs/types/Bool.html) | Optional|
|id|[long](/API_docs/types/long.html) | Yes|Endpoint ID|
|ip|[string](/API_docs/types/string.html) | Yes|IP address of endpoint|
|ipv6|[string](/API_docs/types/string.html) | Yes|IPv6 address of endpoint|
|port|[int](/API_docs/types/int.html) | Yes|Port ID|
|peer\_tag|[bytes](/API_docs/types/bytes.html) | Yes|Our peer tag|



### Type: [PhoneConnection](/API_docs/types/PhoneConnection.html)


### Example:

```
$phoneConnection = ['_' => 'phoneConnection', 'tcp' => Bool, 'id' => long, 'ip' => 'string', 'ipv6' => 'string', 'port' => int, 'peer_tag' => 'bytes'];
```  
