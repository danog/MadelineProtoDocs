---
title: "help.promoData"
description: "MTProxy/Public Service Announcement information"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/help_promoData.html
---
# Constructor: help.promoData  
[Back to constructors index](/API_docs/constructors/index.md)



MTProxy/Public Service Announcement information

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|proxy|[Bool](/API_docs/types/Bool.md) | Optional|MTProxy-related channel|
|expires|[int](/API_docs/types/int.md) | Yes|Expiry of PSA/MTProxy info|
|peer|[Peer](/API_docs/types/Peer.md) | Yes|MTProxy/PSA peer|
|chats|Array of [Chat](/API_docs/types/Chat.md) | Yes|Chat info|
|users|Array of [User](/API_docs/types/User.md) | Yes|User info|
|psa\_type|[string](/API_docs/types/string.md) | Optional|PSA type|
|psa\_message|[string](/API_docs/types/string.md) | Optional|PSA message|



### Type: [help.PromoData](/API_docs/types/help.PromoData.md)


### Example:

```php
$help_promoData = ['_' => 'help.promoData', 'proxy' => Bool, 'expires' => int, 'peer' => Peer, 'chats' => [Chat, Chat], 'users' => [User, User], 'psa_type' => 'string', 'psa_message' => 'string'];
```  
