---
title: "myBoost"
description: "myBoost attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: myBoost  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|slot|[int](/API_docs/types/int.html) | Yes|
|peer|[Peer](/API_docs/types/Peer.html) | Optional|
|date|[int](/API_docs/types/int.html) | Yes|
|expires|[int](/API_docs/types/int.html) | Yes|
|cooldown\_until\_date|[int](/API_docs/types/int.html) | Optional|



### Type: [MyBoost](/API_docs/types/MyBoost.html)


### Example:

```
$myBoost = ['_' => 'myBoost', 'slot' => int, 'peer' => Peer, 'date' => int, 'expires' => int, 'cooldown_until_date' => int];
```  
