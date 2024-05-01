---
title: "phoneConnectionWebrtc"
description: "WebRTC connection parameters"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: phoneConnectionWebrtc  
[Back to constructors index](/API_docs/constructors/index.html)



WebRTC connection parameters

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|turn|[Bool](/API_docs/types/Bool.html) | Optional|Whether this is a TURN endpoint|
|stun|[Bool](/API_docs/types/Bool.html) | Optional|Whether this is a STUN endpoint|
|id|[long](/API_docs/types/long.html) | Yes|Endpoint ID|
|ip|[string](/API_docs/types/string.html) | Yes|IP address|
|ipv6|[string](/API_docs/types/string.html) | Yes|IPv6 address|
|port|[int](/API_docs/types/int.html) | Yes|Port|
|username|[string](/API_docs/types/string.html) | Yes|Username|
|password|[string](/API_docs/types/string.html) | Yes|Password|



### Type: [PhoneConnection](/API_docs/types/PhoneConnection.html)


### Example:

```
$phoneConnectionWebrtc = ['_' => 'phoneConnectionWebrtc', 'turn' => Bool, 'stun' => Bool, 'id' => long, 'ip' => 'string', 'ipv6' => 'string', 'port' => int, 'username' => 'string', 'password' => 'string'];
```  
