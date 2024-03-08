---
title: "myBoost"
description: "Contains information about a single boost slot »."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: myBoost  
[Back to constructors index](/API_docs/constructors/index.html)



Contains information about a single [boost slot »](https://core.telegram.org/api/boost).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|slot|[int](/API_docs/types/int.html) | Yes|[Boost slot ID »](https://core.telegram.org/api/boost)|
|peer|[long](/API_docs/types/long.html) | Optional|If set, indicates this slot is currently occupied, i.e. we are [boosting](https://core.telegram.org/api/boost) this peer.  <br>Note that we can assign multiple boost slots to the same peer.|
|date|[int](/API_docs/types/int.html) | Yes|When (unixtime) we started boosting the `peer`, `0` otherwise.|
|expires|[int](/API_docs/types/int.html) | Yes|Indicates the (unixtime) expiration date of the boost in `peer` (`0` if `peer` is not set).|
|cooldown\_until\_date|[int](/API_docs/types/int.html) | Optional|If `peer` is set, indicates the (unixtime) date after which this boost can be reassigned to another channel.|



### Type: [MyBoost](/API_docs/types/MyBoost.html)


### Example:

```
$myBoost = ['_' => 'myBoost', 'slot' => int, 'peer' => long, 'date' => int, 'expires' => int, 'cooldown_until_date' => int];
```  
