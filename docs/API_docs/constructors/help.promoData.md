---
title: "help.promoData"
description: "A set of useful suggestions and a PSA/MTProxy sponsored peer, see here » for more info."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/help_promoData.html
---
# Constructor: help.promoData  
[Back to constructors index](/API_docs/constructors/index.html)



A set of useful suggestions and a PSA/MTProxy sponsored peer, see [here »](https://core.telegram.org/api/config#suggestions) for more info.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|proxy|[Bool](/API_docs/types/Bool.html) | Optional|Set when connecting using an MTProxy that has configured an associated peer (that will be passed in `peer`, i.e. the channel that sponsored the MTProxy) that should be pinned on top of the chat list.|
|expires|[int](/API_docs/types/int.html) | Yes|Unixtime when to re-invoke [help.getPromoData](../methods/help.getPromoData.html).|
|peer|[long](/API_docs/types/long.html) | Optional|MTProxy/PSA peer|
|psa\_type|[string](/API_docs/types/string.html) | Optional|For Public Service Announcement `peer`s, indicates the type of the PSA.|
|psa\_message|[string](/API_docs/types/string.html) | Optional|For Public Service Announcement `peer`s, contains the PSA itself.|
|pending\_suggestions|Array of [string](/API_docs/types/string.html) | Yes|Contains a list of [pending suggestions »](https://core.telegram.org/api/config#basic-suggestions).|
|dismissed\_suggestions|Array of [string](/API_docs/types/string.html) | Yes|Contains a list of [inverted suggestions »](https://core.telegram.org/api/config#inverted-suggestions).|
|custom\_pending\_suggestion|[PendingSuggestion](/API_docs/types/PendingSuggestion.html) | Optional|Contains a list of [custom pending suggestions »](https://core.telegram.org/api/config#custom-suggestions).|
|chats|Array of [Chat](/API_docs/types/Chat.html) | Yes|Chat info|
|users|Array of [User](/API_docs/types/User.html) | Yes|User info|



### Type: [help.PromoData](/API_docs/types/help.PromoData.html)


### Example:

```
$help_promoData = ['_' => 'help.promoData', 'proxy' => Bool, 'expires' => int, 'peer' => long, 'psa_type' => 'string', 'psa_message' => 'string', 'pending_suggestions' => ['string', 'string'], 'dismissed_suggestions' => ['string', 'string'], 'custom_pending_suggestion' => PendingSuggestion, 'chats' => [Chat, Chat], 'users' => [User, User]];
```  
