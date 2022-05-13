---
title: "phoneCallProtocol"
description: "Protocol info for libtgvoip"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: phoneCallProtocol  
[Back to constructors index](/API_docs/constructors/index.html)



Protocol info for libtgvoip

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|udp\_p2p|[Bool](/API_docs/types/Bool.html) | Optional|Whether to allow P2P connection to the other participant|
|udp\_reflector|[Bool](/API_docs/types/Bool.html) | Optional|Whether to allow connection to the other participants through the reflector servers|
|min\_layer|[int](/API_docs/types/int.html) | Yes|Minimum layer for remote libtgvoip|
|max\_layer|[int](/API_docs/types/int.html) | Yes|Maximum layer for remote libtgvoip|
|library\_versions|Array of [string](/API_docs/types/string.html) | Yes|When using [phone.requestCall](../methods/phone.requestCall.html) and [phone.acceptCall](../methods/phone.acceptCall.html), specify all library versions supported by the client. <br>The server will merge and choose the best library version supported by both peers, returning only the best value in the result of the callee's [phone.acceptCall](../methods/phone.acceptCall.html) and in the [phoneCallAccepted](../constructors/phoneCallAccepted.html) update received by the caller.|



### Type: [PhoneCallProtocol](/API_docs/types/PhoneCallProtocol.html)


### Example:

```
$phoneCallProtocol = ['_' => 'phoneCallProtocol', 'udp_p2p' => Bool, 'udp_reflector' => Bool, 'min_layer' => int, 'max_layer' => int, 'library_versions' => ['string', 'string']];
```  
