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
|archive\_and\_mute\_new\_noncontact\_peers|[Bool](/API_docs/types/Bool.html) | Optional|
|keep\_archived\_unmuted|[Bool](/API_docs/types/Bool.html) | Optional|
|keep\_archived\_folders|[Bool](/API_docs/types/Bool.html) | Optional|
|hide\_read\_marks|[Bool](/API_docs/types/Bool.html) | Optional|
|new\_noncontact\_peers\_require\_premium|[Bool](/API_docs/types/Bool.html) | Optional|



### Type: [GlobalPrivacySettings](/API_docs/types/GlobalPrivacySettings.html)


### Example:

```
$globalPrivacySettings = ['_' => 'globalPrivacySettings', 'archive_and_mute_new_noncontact_peers' => Bool, 'keep_archived_unmuted' => Bool, 'keep_archived_folders' => Bool, 'hide_read_marks' => Bool, 'new_noncontact_peers_require_premium' => Bool];
```  
