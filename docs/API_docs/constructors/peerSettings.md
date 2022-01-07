---
title: "peerSettings"
description: "Peer settings"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: peerSettings  
[Back to constructors index](/API_docs/constructors/index.md)



Peer settings

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|report\_spam|[Bool](/API_docs/types/Bool.md) | Optional|Whether we can still report the user for spam|
|add\_contact|[Bool](/API_docs/types/Bool.md) | Optional|Whether we can add the user as contact|
|block\_contact|[Bool](/API_docs/types/Bool.md) | Optional|Whether we can block the user|
|share\_contact|[Bool](/API_docs/types/Bool.md) | Optional|Whether we can share the user's contact|
|need\_contacts\_exception|[Bool](/API_docs/types/Bool.md) | Optional|Whether a special exception for contacts is needed|
|report\_geo|[Bool](/API_docs/types/Bool.md) | Optional|Whether we can report a geogroup is irrelevant for this location|
|autoarchived|[Bool](/API_docs/types/Bool.md) | Optional|Whether this peer was automatically archived according to [privacy settings](../constructors/globalPrivacySettings.md)|
|invite\_members|[Bool](/API_docs/types/Bool.md) | Optional|
|request\_chat\_broadcast|[Bool](/API_docs/types/Bool.md) | Optional|
|geo\_distance|[int](/API_docs/types/int.md) | Optional|Distance in meters between us and this peer|
|request\_chat\_title|[string](/API_docs/types/string.md) | Optional|
|request\_chat\_date|[int](/API_docs/types/int.md) | Optional|



### Type: [PeerSettings](/API_docs/types/PeerSettings.md)


### Example:

```php
$peerSettings = ['_' => 'peerSettings', 'report_spam' => Bool, 'add_contact' => Bool, 'block_contact' => Bool, 'share_contact' => Bool, 'need_contacts_exception' => Bool, 'report_geo' => Bool, 'autoarchived' => Bool, 'invite_members' => Bool, 'request_chat_broadcast' => Bool, 'geo_distance' => int, 'request_chat_title' => 'string', 'request_chat_date' => int];
```  
