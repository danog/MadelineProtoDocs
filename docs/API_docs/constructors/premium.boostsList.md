---
title: "premium.boostsList"
description: "premium.boostsList attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/premium_boostsList.html
---
# Constructor: premium.boostsList  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|count|[int](/API_docs/types/int.html) | Yes|
|boosts|Array of [Boost](/API_docs/types/Boost.html) | Yes|
|next\_offset|[string](/API_docs/types/string.html) | Optional|
|users|Array of [User](/API_docs/types/User.html) | Yes|



### Type: [premium.BoostsList](/API_docs/types/premium.BoostsList.html)


### Example:

```
$premium_boostsList = ['_' => 'premium.boostsList', 'count' => int, 'boosts' => [Boost, Boost], 'next_offset' => 'string', 'users' => [User, User]];
```  
