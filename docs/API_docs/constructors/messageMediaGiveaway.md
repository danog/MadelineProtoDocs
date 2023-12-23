---
title: "messageMediaGiveaway"
description: "messageMediaGiveaway attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageMediaGiveaway  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|only\_new\_subscribers|[Bool](/API_docs/types/Bool.html) | Optional|
|winners\_are\_visible|[Bool](/API_docs/types/Bool.html) | Optional|
|channels|Array of [long](/API_docs/types/long.html) | Yes|
|countries\_iso2|Array of [string](/API_docs/types/string.html) | Optional|
|prize\_description|[string](/API_docs/types/string.html) | Optional|
|quantity|[int](/API_docs/types/int.html) | Yes|
|months|[int](/API_docs/types/int.html) | Yes|
|until\_date|[int](/API_docs/types/int.html) | Yes|



### Type: [MessageMedia](/API_docs/types/MessageMedia.html)


### Example:

```
$messageMediaGiveaway = ['_' => 'messageMediaGiveaway', 'only_new_subscribers' => Bool, 'winners_are_visible' => Bool, 'channels' => [long, long], 'countries_iso2' => ['string', 'string'], 'prize_description' => 'string', 'quantity' => int, 'months' => int, 'until_date' => int];
```  
