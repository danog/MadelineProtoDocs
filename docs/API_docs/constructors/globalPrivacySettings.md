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
|new\_noncontact\_peers\_require\_premium|[Bool](/API_docs/types/Bool.html) | Optional|If set, only users that have a premium account, are in our contact list, or already have a private chat with us can write to us; a `403 PRIVACY_PREMIUM_REQUIRED` error will be emitted otherwise.  <br>The [userFull](../constructors/userFull.html).`contact_require_premium` flag will be set for users that have this flag enabled.  <br>To check whether we can write to a user with this flag enabled, if we haven't yet cached all the required information (for example we don't have the [userFull](../constructors/userFull.html) or history of all users while displaying the chat list in the sharing UI) the [users.getIsPremiumRequiredToContact](../methods/users.getIsPremiumRequiredToContact.html) method may be invoked, passing the list of users currently visible in the UI, returning a list of booleans that directly specify whether we can or cannot write to each user. <br>This option may be enabled by both non-[Premium](https://core.telegram.org/api/premium) and [Premium](https://core.telegram.org/api/premium) users only if the [new\_noncontact\_peers\_require\_premium\_without\_ownpremium client configuration flag »](https://core.telegram.org/api/config#new-noncontact-peers-require-premium-without-ownpremium) is equal to true, otherwise it may be enabled only by [Premium](https://core.telegram.org/api/premium) users and non-Premium users will receive a `PREMIUM_ACCOUNT_REQUIRED` error when trying to enable this flag.|



### Type: [GlobalPrivacySettings](/API_docs/types/GlobalPrivacySettings.html)


### Example:

```
$globalPrivacySettings = ['_' => 'globalPrivacySettings', 'archive_and_mute_new_noncontact_peers' => Bool, 'keep_archived_unmuted' => Bool, 'keep_archived_folders' => Bool, 'hide_read_marks' => Bool, 'new_noncontact_peers_require_premium' => Bool];
```  
