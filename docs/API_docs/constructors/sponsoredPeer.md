---
title: "sponsoredPeer"
description: "sponsoredPeer attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: sponsoredPeer  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|random\_id|[bytes](/API_docs/types/bytes.html) | Yes|
|peer|[long](/API_docs/types/long.html) | Yes|
|sponsor\_info|[string](/API_docs/types/string.html) | Optional|
|additional\_info|[string](/API_docs/types/string.html) | Optional|



### Type: [SponsoredPeer](/API_docs/types/SponsoredPeer.html)


### Example:

```
$sponsoredPeer = ['_' => 'sponsoredPeer', 'random_id' => 'bytes', 'peer' => long, 'sponsor_info' => 'string', 'additional_info' => 'string'];
```  
