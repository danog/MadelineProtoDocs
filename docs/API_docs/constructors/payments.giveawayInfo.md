---
title: "payments.giveawayInfo"
description: "Contains info about an ongoing giveaway."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/payments_giveawayInfo.html
---
# Constructor: payments.giveawayInfo  
[Back to constructors index](/API_docs/constructors/index.html)



Contains info about an ongoing [giveaway](https://core.telegram.org/api/giveaways).

If neither the `participating`, `joined_too_early_date`, `admin_disallowed_chat_id` or `disallowed_country` flags are set, the user is not currently participating in the giveaway but could participate by joining all the channels specified in the [messageMediaGiveaway](../constructors/messageMediaGiveaway.html).`channels` field.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|participating|[Bool](/API_docs/types/Bool.html) | Optional|The current user is participating in the giveaway.|
|preparing\_results|[Bool](/API_docs/types/Bool.html) | Optional|If set, the giveaway has ended and the results are being prepared.|
|start\_date|[int](/API_docs/types/int.html) | Yes|When was the giveaway started|
|joined\_too\_early\_date|[int](/API_docs/types/int.html) | Optional|The current user can't participate in the giveaway, because they were already a member of the channel when the giveaway started, and the `only_new_subscribers` was set when starting the giveaway.|
|admin\_disallowed\_chat\_id|[long](/API_docs/types/long.html) | Optional|If set, the current user can't participate in the giveaway, because they are an administrator in one of the channels (ID specified in this flag) that created the giveaway.|
|disallowed\_country|[string](/API_docs/types/string.html) | Optional|If set, the current user can't participate in this giveaway, because their phone number is from the specified disallowed country (specified as a two-letter ISO 3166-1 alpha-2 country code).|



### Type: [payments.GiveawayInfo](/API_docs/types/payments.GiveawayInfo.html)


### Example:

```
$payments_giveawayInfo = ['_' => 'payments.giveawayInfo', 'participating' => Bool, 'preparing_results' => Bool, 'start_date' => int, 'joined_too_early_date' => int, 'admin_disallowed_chat_id' => long, 'disallowed_country' => 'string'];
```  
