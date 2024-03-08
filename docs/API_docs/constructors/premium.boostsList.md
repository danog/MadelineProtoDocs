---
title: "premium.boostsList"
description: "List of boosts that were applied to a peer by multiple users."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/premium_boostsList.html
---
# Constructor: premium.boostsList  
[Back to constructors index](/API_docs/constructors/index.html)



List of [boosts](https://core.telegram.org/api/boost) that were applied to a peer by multiple users.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|count|[int](/API_docs/types/int.html) | Yes|Total number of results|
|boosts|Array of [Boost](/API_docs/types/Boost.html) | Yes|[Boosts](https://core.telegram.org/api/boost)|
|next\_offset|[string](/API_docs/types/string.html) | Optional|Offset that can be used for [pagination](https://core.telegram.org/api/offsets).|
|users|Array of [User](/API_docs/types/User.html) | Yes|Mentioned users|



### Type: [premium.BoostsList](/API_docs/types/premium.BoostsList.html)


### Example:

```
$premium_boostsList = ['_' => 'premium.boostsList', 'count' => int, 'boosts' => [Boost, Boost], 'next_offset' => 'string', 'users' => [User, User]];
```  
