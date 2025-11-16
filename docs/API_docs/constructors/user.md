---
title: "user"
description: "Indicates info about a certain user."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: user  
[Back to constructors index](/API_docs/constructors/index.html)



Indicates info about a certain user.

Unless specified otherwise, when updating the [local peer database](https://core.telegram.org/api/peers), all fields from the newly received constructor take priority over the old constructor cached locally (including by removing fields that aren't set in the new constructor).

See [here »](https://github.com/tdlib/td/blob/cb164927417f22811c74cd8678ed4a5ab7cb80ba/td/telegram/UserManager.cpp#L2267) for an implementation of the logic to use when updating the [local user peer database](https://core.telegram.org/api/peers).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|self|[Bool](/API_docs/types/Bool.html) | Optional|Whether this user indicates the currently logged in user|
|contact|[Bool](/API_docs/types/Bool.html) | Optional|Whether this user is a contact <br>When updating the [local peer database](https://core.telegram.org/api/peers), do not apply changes to this field if the `min` flag is set.|
|mutual\_contact|[Bool](/API_docs/types/Bool.html) | Optional|Whether this user is a mutual contact. <br>When updating the [local peer database](https://core.telegram.org/api/peers), do not apply changes to this field if the `min` flag is set.|
|deleted|[Bool](/API_docs/types/Bool.html) | Optional|Whether the account of this user was deleted. <br>Changes to this flag should invalidate the local [userFull](../constructors/userFull.html) cache for this user ID, see [here »](https://core.telegram.org/api/peers#full-info-database) for more info.|
|bot|[Bool](/API_docs/types/Bool.html) | Optional|Is this user a bot? <br>Changes to this flag should invalidate the local [userFull](../constructors/userFull.html) cache for this user ID, see [here »](https://core.telegram.org/api/peers#full-info-database) for more info.|
|bot\_chat\_history|[Bool](/API_docs/types/Bool.html) | Optional|Can the bot see all messages in groups?|
|bot\_nochats|[Bool](/API_docs/types/Bool.html) | Optional|Can the bot be added to groups?|
|verified|[Bool](/API_docs/types/Bool.html) | Optional|Whether this user is verified|
|restricted|[Bool](/API_docs/types/Bool.html) | Optional|Access to this user must be restricted for the reason specified in `restriction_reason`|
|min|[Bool](/API_docs/types/Bool.html) | Optional|See [min](https://core.telegram.org/api/min)|
|bot\_inline\_geo|[Bool](/API_docs/types/Bool.html) | Optional|Whether the bot can request our geolocation in inline mode|
|support|[Bool](/API_docs/types/Bool.html) | Optional|Whether this is an official support user|
|scam|[Bool](/API_docs/types/Bool.html) | Optional|This may be a scam user|
|apply\_min\_photo|[Bool](/API_docs/types/Bool.html) | Optional|If set and `min` is set, the value of `photo` can be used to update the local database, see the documentation of that flag for more info.|
|fake|[Bool](/API_docs/types/Bool.html) | Optional|If set, this user was reported by many users as a fake or scam user: be careful when interacting with them.|
|bot\_attach\_menu|[Bool](/API_docs/types/Bool.html) | Optional|Whether this bot offers an [attachment menu web app](https://core.telegram.org/api/bots/attach)|
|premium|[Bool](/API_docs/types/Bool.html) | Optional|Whether this user is a Telegram Premium user <br>Changes to this flag should invalidate the local [userFull](../constructors/userFull.html) cache for this user ID, see [here »](https://core.telegram.org/api/peers#full-info-database) for more info. <br>Changes to this flag if the `self` flag is set should also trigger the following calls, to refresh the respective caches: <br>- The [help.getConfig](../methods/help.getConfig.html) cache <br>- The [messages.getTopReactions](../methods/messages.getTopReactions.html) cache if the `bot` flag is **not** set|
|attach\_menu\_enabled|[Bool](/API_docs/types/Bool.html) | Optional|Whether we installed the [attachment menu web app](https://core.telegram.org/api/bots/attach) offered by this bot. <br>When updating the [local peer database](https://core.telegram.org/api/peers), do not apply changes to this field if the `min` flag is set.|
|bot\_can\_edit|[Bool](/API_docs/types/Bool.html) | Optional|
|close\_friend|[Bool](/API_docs/types/Bool.html) | Optional|
|stories\_hidden|[Bool](/API_docs/types/Bool.html) | Optional|
|stories\_unavailable|[Bool](/API_docs/types/Bool.html) | Optional|
|contact\_require\_premium|[Bool](/API_docs/types/Bool.html) | Optional|
|bot\_business|[Bool](/API_docs/types/Bool.html) | Optional|
|bot\_has\_main\_app|[Bool](/API_docs/types/Bool.html) | Optional|
|bot\_forum\_view|[Bool](/API_docs/types/Bool.html) | Optional|
|id|[long](/API_docs/types/long.html) | Yes|ID of the user, see [here »](https://core.telegram.org/api/peers#peer-id) for more info and the available ID range.|
|access\_hash|[long](/API_docs/types/long.html) | Optional|Access hash of the user, see [here »](https://core.telegram.org/api/peers#access-hash) for more info. <br>If this flag is set, when updating the [local peer database](https://core.telegram.org/api/peers), generate a virtual flag called `min_access_hash`, which is: <br>- Set to `true` if `min` is set AND <br>-- The `phone` flag is **not** set OR <br>-- The `phone` flag is set and the associated phone number string is non-empty <br>- Set to `false` otherwise. <br><br>Then, apply both `access_hash` and `min_access_hash` to the local database if: <br>- `min_access_hash` is false OR <br>- `min_access_hash` is true AND <br>-- There is no locally cached object for this user OR <br>-- There is no `access_hash` in the local cache OR <br>-- The cached object's `min_access_hash` is also true <br><br>If the final merged object stored to the database has the `min_access_hash` field set to true, the related `access_hash` is **only** suitable to use in [`inputPeerPhotoFileLocation` »](../constructors/inputPeerPhotoFileLocation.html), to directly [download the profile pictures](https://core.telegram.org/api/files) of users, everywhere else a `inputPeer*FromMessage` constructor will have to be generated as specified [here »](https://core.telegram.org/api/min). <br>Bots can also use min access hashes in some conditions, by passing `0` instead of the min access hash.|
|first\_name|[string](/API_docs/types/string.html) | Optional|First name. <br>When updating the [local peer database](https://core.telegram.org/api/peers), apply changes to this field only if: <br>- The `min` flag is not set OR <br>- The `min` flag is set AND <br>-- The `min` flag of the locally cached user entry is set.|
|last\_name|[string](/API_docs/types/string.html) | Optional|Last name. <br>When updating the [local peer database](https://core.telegram.org/api/peers), apply changes to this field only if: <br>- The `min` flag is not set OR <br>- The `min` flag is set AND <br>-- The `min` flag of the locally cached user entry is set.|
|username|[string](/API_docs/types/string.html) | Optional|Main active username. <br>When updating the [local peer database](https://core.telegram.org/api/peers), apply changes to this field only if: <br>- The `min` flag is not set OR <br>- The `min` flag is set AND <br>-- The `min` flag of the locally cached user entry is set. <br>Changes to this flag should invalidate the local [userFull](../constructors/userFull.html) cache for this user ID if the above conditions are respected and the `bot_can_edit` flag is also set.|
|phone|[string](/API_docs/types/string.html) | Optional|Phone number. <br>When updating the [local peer database](https://core.telegram.org/api/peers), apply changes to this field only if: <br>- The `min` flag is not set OR <br>- The `min` flag is set AND <br>-- The `min` flag of the locally cached user entry is set.|
|photo|[UserProfilePhoto](/API_docs/types/UserProfilePhoto.html) | Optional|Profile picture of user. <br>When updating the [local peer database](https://core.telegram.org/api/peers), apply changes to this field only if: <br>- The `min` flag is not set OR <br>- The `min` flag is set AND <br>-- The `apply_min_photo` flag is set OR <br>-- The `min` flag of the locally cached user entry is set.|
|status|[UserStatus](/API_docs/types/UserStatus.html) | Optional|Online status of user. <br>When updating the [local peer database](https://core.telegram.org/api/peers), apply changes to this field only if: <br>- The `min` flag is not set OR <br>- The `min` flag is set AND <br>-- The `min` flag of the locally cached user entry is set OR <br>-- The locally cached user entry is equal to [userStatusEmpty](../constructors/userStatusEmpty.html).|
|bot\_info\_version|[int](/API_docs/types/int.html) | Optional|Version of the [bot\_info field in userFull](../constructors/userFull.html), incremented every time it changes. <br>Changes to this flag should invalidate the local [userFull](../constructors/userFull.html) cache for this user ID, see [here »](https://core.telegram.org/api/peers#full-info-database) for more info.|
|restriction\_reason|Array of [RestrictionReason](/API_docs/types/RestrictionReason.html) | Optional|Contains the reason why access to this user must be restricted.|
|bot\_inline\_placeholder|[string](/API_docs/types/string.html) | Optional|Inline placeholder for this inline bot|
|lang\_code|[string](/API_docs/types/string.html) | Optional|Language code of the user|
|emoji\_status|[EmojiStatus](/API_docs/types/EmojiStatus.html) | Optional|[Emoji status](https://core.telegram.org/api/emoji-status)|
|usernames|Array of [Username](/API_docs/types/Username.html) | Optional|
|stories\_max\_id|[RecentStory](/API_docs/types/RecentStory.html) | Optional|
|color|[PeerColor](/API_docs/types/PeerColor.html) | Optional|
|profile\_color|[PeerColor](/API_docs/types/PeerColor.html) | Optional|
|bot\_active\_users|[int](/API_docs/types/int.html) | Optional|
|bot\_verification\_icon|[long](/API_docs/types/long.html) | Optional|
|send\_paid\_messages\_stars|[long](/API_docs/types/long.html) | Optional|



### Type: [User](/API_docs/types/User.html)


### Example:

```
$user = ['_' => 'user', 'self' => Bool, 'contact' => Bool, 'mutual_contact' => Bool, 'deleted' => Bool, 'bot' => Bool, 'bot_chat_history' => Bool, 'bot_nochats' => Bool, 'verified' => Bool, 'restricted' => Bool, 'min' => Bool, 'bot_inline_geo' => Bool, 'support' => Bool, 'scam' => Bool, 'apply_min_photo' => Bool, 'fake' => Bool, 'bot_attach_menu' => Bool, 'premium' => Bool, 'attach_menu_enabled' => Bool, 'bot_can_edit' => Bool, 'close_friend' => Bool, 'stories_hidden' => Bool, 'stories_unavailable' => Bool, 'contact_require_premium' => Bool, 'bot_business' => Bool, 'bot_has_main_app' => Bool, 'bot_forum_view' => Bool, 'id' => long, 'access_hash' => long, 'first_name' => 'string', 'last_name' => 'string', 'username' => 'string', 'phone' => 'string', 'photo' => UserProfilePhoto, 'status' => UserStatus, 'bot_info_version' => int, 'restriction_reason' => [RestrictionReason, RestrictionReason], 'bot_inline_placeholder' => 'string', 'lang_code' => 'string', 'emoji_status' => EmojiStatus, 'usernames' => [Username, Username], 'stories_max_id' => RecentStory, 'color' => PeerColor, 'profile_color' => PeerColor, 'bot_active_users' => int, 'bot_verification_icon' => long, 'send_paid_messages_stars' => long];
```  
