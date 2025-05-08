---
title: "help.promoData"
description: "MTProxy/Public Service Announcement information"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/help_promoData.html
---
# Constructor: help.promoData  
[Back to constructors index](/API_docs/constructors/index.html)



MTProxy/Public Service Announcement information

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|proxy|[Bool](/API_docs/types/Bool.html) | Optional|MTProxy-related channel|
|expires|[int](/API_docs/types/int.html) | Yes|Expiry of PSA/MTProxy info|
|peer|[long](/API_docs/types/long.html) | Optional|MTProxy/PSA peer|
|psa\_type|[string](/API_docs/types/string.html) | Optional|PSA type|
|psa\_message|[string](/API_docs/types/string.html) | Optional|PSA message|
|pending\_suggestions|Array of [string](/API_docs/types/string.html) | Yes|
|dismissed\_suggestions|Array of [string](/API_docs/types/string.html) | Yes|
|custom\_pending\_suggestion|[PendingSuggestion](/API_docs/types/PendingSuggestion.html) | Optional|
|chats|Array of [Chat](/API_docs/types/Chat.html) | Yes|Chat info|
|users|Array of [User](/API_docs/types/User.html) | Yes|User info|



### Type: [help.PromoData](/API_docs/types/help.PromoData.html)


### Example:

```
$help_promoData = ['_' => 'help.promoData', 'proxy' => Bool, 'expires' => int, 'peer' => long, 'psa_type' => 'string', 'psa_message' => 'string', 'pending_suggestions' => ['string', 'string'], 'dismissed_suggestions' => ['string', 'string'], 'custom_pending_suggestion' => PendingSuggestion, 'chats' => [Chat, Chat], 'users' => [User, User]];
```  
