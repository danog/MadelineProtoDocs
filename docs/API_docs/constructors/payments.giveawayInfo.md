---
title: "payments.giveawayInfo"
description: "payments.giveawayInfo attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/payments_giveawayInfo.html
---
# Constructor: payments.giveawayInfo  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|participating|[Bool](/API_docs/types/Bool.html) | Optional|
|preparing\_results|[Bool](/API_docs/types/Bool.html) | Optional|
|start\_date|[int](/API_docs/types/int.html) | Yes|
|joined\_too\_early\_date|[int](/API_docs/types/int.html) | Optional|
|admin\_disallowed\_chat\_id|[long](/API_docs/types/long.html) | Optional|
|disallowed\_country|[string](/API_docs/types/string.html) | Optional|



### Type: [payments.GiveawayInfo](/API_docs/types/payments.GiveawayInfo.html)


### Example:

```
$payments_giveawayInfo = ['_' => 'payments.giveawayInfo', 'participating' => Bool, 'preparing_results' => Bool, 'start_date' => int, 'joined_too_early_date' => int, 'admin_disallowed_chat_id' => long, 'disallowed_country' => 'string'];
```  
