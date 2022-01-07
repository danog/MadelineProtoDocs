---
title: "user"
description: "Indicates info about a certain user"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: user  
[Back to constructors index](/API_docs/constructors/index.md)



Indicates info about a certain user

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|self|[Bool](/API_docs/types/Bool.md) | Optional|Whether this user indicates the currently logged in user|
|contact|[Bool](/API_docs/types/Bool.md) | Optional|Whether this user is a contact|
|mutual\_contact|[Bool](/API_docs/types/Bool.md) | Optional|Whether this user is a mutual contact|
|deleted|[Bool](/API_docs/types/Bool.md) | Optional|Whether the account of this user was deleted|
|bot|[Bool](/API_docs/types/Bool.md) | Optional|Is this user a bot?|
|bot\_chat\_history|[Bool](/API_docs/types/Bool.md) | Optional|Can the bot see all messages in groups?|
|bot\_nochats|[Bool](/API_docs/types/Bool.md) | Optional|Can the bot be added to groups?|
|verified|[Bool](/API_docs/types/Bool.md) | Optional|Whether this user is verified|
|restricted|[Bool](/API_docs/types/Bool.md) | Optional|Access to this user must be restricted for the reason specified in `restriction_reason`|
|min|[Bool](/API_docs/types/Bool.md) | Optional|See [min](https://core.telegram.org/api/min)|
|bot\_inline\_geo|[Bool](/API_docs/types/Bool.md) | Optional|Whether the bot can request our geolocation in inline mode|
|support|[Bool](/API_docs/types/Bool.md) | Optional|Whether this is an official support user|
|scam|[Bool](/API_docs/types/Bool.md) | Optional|This may be a scam user|
|apply\_min\_photo|[Bool](/API_docs/types/Bool.md) | Optional|If set, the profile picture for this user should be refetched|
|fake|[Bool](/API_docs/types/Bool.md) | Optional|
|id|[long](/API_docs/types/long.md) | Yes|
|access\_hash|[long](/API_docs/types/long.md) | Optional|Access hash of the user|
|first\_name|[string](/API_docs/types/string.md) | Optional|First name|
|last\_name|[string](/API_docs/types/string.md) | Optional|Last name|
|username|[string](/API_docs/types/string.md) | Optional|Username|
|phone|[string](/API_docs/types/string.md) | Optional|Phone number|
|photo|[UserProfilePhoto](/API_docs/types/UserProfilePhoto.md) | Optional|Profile picture of user|
|status|[UserStatus](/API_docs/types/UserStatus.md) | Optional|Online status of user|
|bot\_info\_version|[int](/API_docs/types/int.md) | Optional|Version of the [bot\_info field in userFull](../constructors/userFull.md), incremented every time it changes|
|restriction\_reason|Array of [RestrictionReason](/API_docs/types/RestrictionReason.md) | Optional|Contains the reason why access to this user must be restricted.|
|bot\_inline\_placeholder|[string](/API_docs/types/string.md) | Optional|Inline placeholder for this inline bot|
|lang\_code|[string](/API_docs/types/string.md) | Optional|Language code of the user|



### Type: [User](/API_docs/types/User.md)


### Example:

```php
$user = ['_' => 'user', 'self' => Bool, 'contact' => Bool, 'mutual_contact' => Bool, 'deleted' => Bool, 'bot' => Bool, 'bot_chat_history' => Bool, 'bot_nochats' => Bool, 'verified' => Bool, 'restricted' => Bool, 'min' => Bool, 'bot_inline_geo' => Bool, 'support' => Bool, 'scam' => Bool, 'apply_min_photo' => Bool, 'fake' => Bool, 'id' => long, 'access_hash' => long, 'first_name' => 'string', 'last_name' => 'string', 'username' => 'string', 'phone' => 'string', 'photo' => UserProfilePhoto, 'status' => UserStatus, 'bot_info_version' => int, 'restriction_reason' => [RestrictionReason, RestrictionReason], 'bot_inline_placeholder' => 'string', 'lang_code' => 'string'];
```  
