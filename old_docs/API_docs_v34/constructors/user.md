---
title: user
description: Indicates info about a certain user
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: user  
[Back to constructors index](index.md)



Indicates info about a certain user

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|self|[Bool](../types/Bool.md) | Optional|Whether this user indicates the currently logged in user|
|contact|[Bool](../types/Bool.md) | Optional|Whether this user is a contact|
|mutual\_contact|[Bool](../types/Bool.md) | Optional|Whether this user is a mutual contact|
|deleted|[Bool](../types/Bool.md) | Optional|Whether the account of this user was deleted|
|bot|[Bool](../types/Bool.md) | Optional|Is this user a bot?|
|bot\_chat\_history|[Bool](../types/Bool.md) | Optional|Can the bot see all messages in groups?|
|bot\_nochats|[Bool](../types/Bool.md) | Optional|Can the bot be added to groups?|
|verified|[Bool](../types/Bool.md) | Optional|Whether this user is verified|
|restricted|[Bool](../types/Bool.md) | Optional|Access to this user must be restricted for the reason specified in `restriction_reason`|
|min|[Bool](../types/Bool.md) | Optional|See [min](https://core.telegram.org/api/min)|
|bot\_inline\_geo|[Bool](../types/Bool.md) | Optional|Whether the bot can request our geolocation in inline mode|
|support|[Bool](../types/Bool.md) | Optional|Whether this is an official support user|
|scam|[Bool](../types/Bool.md) | Optional|This may be a scam user|
|id|[int](../types/int.md) | Yes|ID of the user|
|access\_hash|[long](../types/long.md) | Optional|Access hash of the user|
|first\_name|[string](../types/string.md) | Optional|First name|
|last\_name|[string](../types/string.md) | Optional|Last name|
|username|[string](../types/string.md) | Optional|Username|
|phone|[string](../types/string.md) | Optional|Phone number|
|photo|[UserProfilePhoto](../types/UserProfilePhoto.md) | Optional|Profile picture of user|
|status|[UserStatus](../types/UserStatus.md) | Optional|Online status of user|
|bot\_info\_version|[int](../types/int.md) | Optional|Version of the [bot\_info field in userFull](../constructors/userFull.md), incremented every time it changes|
|restriction\_reason|[string](../types/string.md) | Optional|
|bot\_inline\_placeholder|[string](../types/string.md) | Optional|Inline placeholder for this inline bot|
|lang\_code|[string](../types/string.md) | Optional|Language code of the user|



### Type: [User](../types/User.md)


### Example:

```php
$user = ['_' => 'user', 'self' => Bool, 'contact' => Bool, 'mutual_contact' => Bool, 'deleted' => Bool, 'bot' => Bool, 'bot_chat_history' => Bool, 'bot_nochats' => Bool, 'verified' => Bool, 'restricted' => Bool, 'min' => Bool, 'bot_inline_geo' => Bool, 'support' => Bool, 'scam' => Bool, 'id' => int, 'access_hash' => long, 'first_name' => 'string', 'last_name' => 'string', 'username' => 'string', 'phone' => 'string', 'photo' => UserProfilePhoto, 'status' => UserStatus, 'bot_info_version' => int, 'restriction_reason' => 'string', 'bot_inline_placeholder' => 'string', 'lang_code' => 'string'];
```  


Or, if you're into Lua:

```lua
user={_='user', self=Bool, contact=Bool, mutual_contact=Bool, deleted=Bool, bot=Bool, bot_chat_history=Bool, bot_nochats=Bool, verified=Bool, restricted=Bool, min=Bool, bot_inline_geo=Bool, support=Bool, scam=Bool, id=int, access_hash=long, first_name='string', last_name='string', username='string', phone='string', photo=UserProfilePhoto, status=UserStatus, bot_info_version=int, restriction_reason='string', bot_inline_placeholder='string', lang_code='string'}

```


