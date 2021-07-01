---
title: globalPrivacySettings
description: Global privacy settings
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: globalPrivacySettings  
[Back to constructors index](index.md)



Global privacy settings

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|archive\_and\_mute\_new\_noncontact\_peers|[Bool](../types/Bool.md) | Optional|Whether to archive and mute new chats from non-contacts|



### Type: [GlobalPrivacySettings](../types/GlobalPrivacySettings.md)


### Example:

```php
$globalPrivacySettings = ['_' => 'globalPrivacySettings', 'archive_and_mute_new_noncontact_peers' => Bool];
```  


Or, if you're into Lua:

```lua
globalPrivacySettings={_='globalPrivacySettings', archive_and_mute_new_noncontact_peers=Bool}

```


