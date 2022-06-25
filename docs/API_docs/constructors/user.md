---
title: "user"
description: "Indicates info about a certain user"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: user  
[Back to constructors index](/API_docs/constructors/index.html)



Indicates info about a certain user

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|self|[Bool](/API_docs/types/Bool.html) | Optional|Whether this user indicates the currently logged in user|
|contact|[Bool](/API_docs/types/Bool.html) | Optional|Whether this user is a contact|
|mutual\_contact|[Bool](/API_docs/types/Bool.html) | Optional|Whether this user is a mutual contact|
|deleted|[Bool](/API_docs/types/Bool.html) | Optional|Whether the account of this user was deleted|
|bot|[Bool](/API_docs/types/Bool.html) | Optional|Is this user a bot?|
|bot\_chat\_history|[Bool](/API_docs/types/Bool.html) | Optional|Can the bot see all messages in groups?|
|bot\_nochats|[Bool](/API_docs/types/Bool.html) | Optional|Can the bot be added to groups?|
|verified|[Bool](/API_docs/types/Bool.html) | Optional|Whether this user is verified|
|restricted|[Bool](/API_docs/types/Bool.html) | Optional|Access to this user must be restricted for the reason specified in `restriction_reason`|
|min|[Bool](/API_docs/types/Bool.html) | Optional|See [min](https://core.telegram.org/api/min)|
|bot\_inline\_geo|[Bool](/API_docs/types/Bool.html) | Optional|Whether the bot can request our geolocation in inline mode|
|support|[Bool](/API_docs/types/Bool.html) | Optional|Whether this is an official support user|
|scam|[Bool](/API_docs/types/Bool.html) | Optional|This may be a scam user|
|apply\_min\_photo|[Bool](/API_docs/types/Bool.html) | Optional|If set, the profile picture for this user should be refetched|
|fake|[Bool](/API_docs/types/Bool.html) | Optional|If set, this user was reported by many users as a fake or scam user: be careful when interacting with them.|
|bot\_attach\_menu|[Bool](/API_docs/types/Bool.html) | Optional|
|premium|[Bool](/API_docs/types/Bool.html) | Optional|
|attach\_menu\_enabled|[Bool](/API_docs/types/Bool.html) | Optional|
|id|[long](/API_docs/types/long.html) | Yes|ID of the user|
|access\_hash|[long](/API_docs/types/long.html) | Optional|Access hash of the user|
|first\_name|[string](/API_docs/types/string.html) | Optional|First name|
|last\_name|[string](/API_docs/types/string.html) | Optional|Last name|
|username|[string](/API_docs/types/string.html) | Optional|Username|
|phone|[string](/API_docs/types/string.html) | Optional|Phone number|
|photo|[UserProfilePhoto](/API_docs/types/UserProfilePhoto.html) | Optional|Profile picture of user|
|status|[UserStatus](/API_docs/types/UserStatus.html) | Optional|Online status of user|
|bot\_info\_version|[int](/API_docs/types/int.html) | Optional|Version of the [bot\_info field in userFull](../constructors/userFull.html), incremented every time it changes|
|restriction\_reason|Array of [RestrictionReason](/API_docs/types/RestrictionReason.html) | Optional|Contains the reason why access to this user must be restricted.|
|bot\_inline\_placeholder|[string](/API_docs/types/string.html) | Optional|Inline placeholder for this inline bot|
|lang\_code|[string](/API_docs/types/string.html) | Optional|Language code of the user|



### Type: [User](/API_docs/types/User.html)


### Example:

```
$user = ['_' => 'user', 'self' => Bool, 'contact' => Bool, 'mutual_contact' => Bool, 'deleted' => Bool, 'bot' => Bool, 'bot_chat_history' => Bool, 'bot_nochats' => Bool, 'verified' => Bool, 'restricted' => Bool, 'min' => Bool, 'bot_inline_geo' => Bool, 'support' => Bool, 'scam' => Bool, 'apply_min_photo' => Bool, 'fake' => Bool, 'bot_attach_menu' => Bool, 'premium' => Bool, 'attach_menu_enabled' => Bool, 'id' => long, 'access_hash' => long, 'first_name' => 'string', 'last_name' => 'string', 'username' => 'string', 'phone' => 'string', 'photo' => UserProfilePhoto, 'status' => UserStatus, 'bot_info_version' => int, 'restriction_reason' => [RestrictionReason, RestrictionReason], 'bot_inline_placeholder' => 'string', 'lang_code' => 'string'];
```  
