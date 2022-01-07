---
title: "help.promoData"
description: "MTProxy/Public Service Announcement information"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/help_promoData.html
---
# Constructor: help.promoData  
[Back to constructors index](index.md)



MTProxy/Public Service Announcement information

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|proxy|[Bool](../types/Bool.md) | Optional|MTProxy-related channel|
|expires|[int](../types/int.md) | Yes|Expiry of PSA/MTProxy info|
|peer|[Peer](../types/Peer.md) | Yes|MTProxy/PSA peer|
|chats|Array of [Chat](../types/Chat.md) | Yes|Chat info|
|users|Array of [User](../types/User.md) | Yes|User info|
|psa\_type|[string](../types/string.md) | Optional|PSA type|
|psa\_message|[string](../types/string.md) | Optional|PSA message|



### Type: [help.PromoData](../types/help.PromoData.md)


### Example:

```php
$help_promoData = ['_' => 'help.promoData', 'proxy' => Bool, 'expires' => int, 'peer' => Peer, 'chats' => [Chat, Chat], 'users' => [User, User], 'psa_type' => 'string', 'psa_message' => 'string'];
```  
