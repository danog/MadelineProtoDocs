---
title: "globalPrivacySettings"
description: "Global privacy settings"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: globalPrivacySettings  
[Back to constructors index](/API_docs/constructors/index.html)



Global privacy settings

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|archive\_and\_mute\_new\_noncontact\_peers|[Bool](/API_docs/types/Bool.html) | Optional|Whether to archive and mute new chats from non-contacts|
|keep\_archived\_unmuted|[Bool](/API_docs/types/Bool.html) | Optional|Whether unmuted chats will be kept in the Archive chat list when they get a new message.|
|keep\_archived\_folders|[Bool](/API_docs/types/Bool.html) | Optional|Whether unmuted chats that are always included or pinned in a [folder](https://core.telegram.org/api/folders), will be kept in the Archive chat list when they get a new message. Ignored if `keep_archived_unmuted` is set.|
|hide\_read\_marks|[Bool](/API_docs/types/Bool.html) | Optional|If this flag is set, the [inputPrivacyKeyStatusTimestamp](../constructors/inputPrivacyKeyStatusTimestamp.html) key will also apply to the ability to use [messages.getOutboxReadDate](../methods/messages.getOutboxReadDate.html) on messages sent to us. <br>Meaning, users that cannot see *our* exact last online date due to the current value of the [inputPrivacyKeyStatusTimestamp](../constructors/inputPrivacyKeyStatusTimestamp.html) key will receive a `403 USER_PRIVACY_RESTRICTED` error when invoking [messages.getOutboxReadDate](../methods/messages.getOutboxReadDate.html) to fetch the exact read date of a message they sent to us. <br>The [userFull](../constructors/userFull.html).`read_dates_private` flag will be set for users that have this flag enabled.|
|new\_noncontact\_peers\_require\_premium|[Bool](/API_docs/types/Bool.html) | Optional|See [here for more info on this flag »](https://core.telegram.org/api/privacy#require-premium-for-new-non-contact-users).|
|display\_gifts\_button|[Bool](/API_docs/types/Bool.html) | Optional|Enables or disables our [userFull](../constructors/userFull.html).`display_gifts_button` flag: if the [userFull](../constructors/userFull.html).`display_gifts_button` flag of both us and another user is set, a gift button should always be displayed in the text field in private chats with the other user: once clicked, the gift UI should be displayed, offering the user options to gift [Telegram Premium »](https://core.telegram.org/api/premium#gifting-telegram-premium) subscriptions or [Telegram Gifts »](https://core.telegram.org/api/gifts).|
|noncontact\_peers\_paid\_stars|[long](/API_docs/types/long.html) | Optional|If configured, specifies the number of [stars](https://core.telegram.org/api/stars) users must pay us to send us a message, see [here »](https://core.telegram.org/api/paid-messages) for more info on paid messages.|
|disallowed\_gifts|[DisallowedGiftsSettings](/API_docs/types/DisallowedGiftsSettings.html) | Optional|Disallows the reception of specific gift types.|



### Type: [GlobalPrivacySettings](/API_docs/types/GlobalPrivacySettings.html)


### Example:

```
$globalPrivacySettings = ['_' => 'globalPrivacySettings', 'archive_and_mute_new_noncontact_peers' => Bool, 'keep_archived_unmuted' => Bool, 'keep_archived_folders' => Bool, 'hide_read_marks' => Bool, 'new_noncontact_peers_require_premium' => Bool, 'display_gifts_button' => Bool, 'noncontact_peers_paid_stars' => long, 'disallowed_gifts' => DisallowedGiftsSettings];
```  
