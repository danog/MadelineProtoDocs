---
title: "sponsoredPeer"
description: "A sponsored peer."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: sponsoredPeer  
[Back to constructors index](/API_docs/constructors/index.html)



A sponsored peer.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|random\_id|[bytes](/API_docs/types/bytes.html) | Yes|ID of the sponsored peer, to be passed to [messages.viewSponsoredMessage](../methods/messages.viewSponsoredMessage.html), [messages.clickSponsoredMessage](../methods/messages.clickSponsoredMessage.html) or [messages.reportSponsoredMessage](../methods/messages.reportSponsoredMessage.html) (the same methods used for [sponsored messages &amp;raquo](https://core.telegram.org/api/sponsored-messages)).|
|peer|[long](/API_docs/types/long.html) | Yes|The sponsored peer.|
|sponsor\_info|[string](/API_docs/types/string.html) | Optional|If set, contains additional information about the sponsor to be shown along with the peer.|
|additional\_info|[string](/API_docs/types/string.html) | Optional|If set, contains additional information about the sponsored message to be shown along with the peer.|



### Type: [SponsoredPeer](/API_docs/types/SponsoredPeer.html)


### Example:

```
$sponsoredPeer = ['_' => 'sponsoredPeer', 'random_id' => 'bytes', 'peer' => long, 'sponsor_info' => 'string', 'additional_info' => 'string'];
```  
