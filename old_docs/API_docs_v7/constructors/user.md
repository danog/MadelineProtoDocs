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
|id|[int](../types/int.md) | Yes|ID of the user|
|access\_hash|[long](../types/long.md) | Optional|Access hash of the user|
|first\_name|[string](../types/string.md) | Optional|First name|
|last\_name|[string](../types/string.md) | Optional|Last name|
|username|[string](../types/string.md) | Optional|Username|
|phone|[string](../types/string.md) | Optional|Phone number|
|photo|[UserProfilePhoto](../types/UserProfilePhoto.md) | Optional|Profile picture of user|
|status|[UserStatus](../types/UserStatus.md) | Optional|Online status of user|
|bot\_info\_version|[int](../types/int.md) | Optional|Version of the [bot\_info field in userFull](../constructors/userFull.md), incremented every time it changes|



### Type: [User](../types/User.md)


### Example:

```php
$user = ['_' => 'user', 'self' => Bool, 'contact' => Bool, 'mutual_contact' => Bool, 'deleted' => Bool, 'bot' => Bool, 'bot_chat_history' => Bool, 'bot_nochats' => Bool, 'verified' => Bool, 'id' => int, 'access_hash' => long, 'first_name' => 'string', 'last_name' => 'string', 'username' => 'string', 'phone' => 'string', 'photo' => UserProfilePhoto, 'status' => UserStatus, 'bot_info_version' => int];
```  


Or, if you're into Lua:

```lua
user={_='user', self=Bool, contact=Bool, mutual_contact=Bool, deleted=Bool, bot=Bool, bot_chat_history=Bool, bot_nochats=Bool, verified=Bool, id=int, access_hash=long, first_name='string', last_name='string', username='string', phone='string', photo=UserProfilePhoto, status=UserStatus, bot_info_version=int}

```


