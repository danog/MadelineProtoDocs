---
title: "stories.boostersList"
description: "stories.boostersList attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/stories_boostersList.html
---
# Constructor: stories.boostersList  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|count|[int](/API_docs/types/int.html) | Yes|
|boosters|Array of [Booster](/API_docs/types/Booster.html) | Yes|
|next\_offset|[string](/API_docs/types/string.html) | Optional|
|users|Array of [User](/API_docs/types/User.html) | Yes|



### Type: [stories.BoostersList](/API_docs/types/stories.BoostersList.html)


### Example:

```
$stories_boostersList = ['_' => 'stories.boostersList', 'count' => int, 'boosters' => [Booster, Booster], 'next_offset' => 'string', 'users' => [User, User]];
```  
