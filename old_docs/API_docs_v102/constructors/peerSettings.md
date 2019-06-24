---
title: peerSettings
description: Peer settings
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: peerSettings  
[Back to constructors index](index.md)



Peer settings

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|report\_spam|[Bool](../types/Bool.md) | Optional|Report spam?|
|add\_contact|[Bool](../types/Bool.md) | Optional|Can add as a contact?|
|block\_contact|[Bool](../types/Bool.md) | Optional|Block contact|
|share\_contact|[Bool](../types/Bool.md) | Optional|Share contact|
|need\_contacts\_exception|[Bool](../types/Bool.md) | Optional|Contact exception|
|report\_geo|[Bool](../types/Bool.md) | Optional|Geotype|



### Type: [PeerSettings](../types/PeerSettings.md)


### Example:

```php
$peerSettings = ['_' => 'peerSettings', 'report_spam' => Bool, 'add_contact' => Bool, 'block_contact' => Bool, 'share_contact' => Bool, 'need_contacts_exception' => Bool, 'report_geo' => Bool];
```  


Or, if you're into Lua:

```lua
peerSettings={_='peerSettings', report_spam=Bool, add_contact=Bool, block_contact=Bool, share_contact=Bool, need_contacts_exception=Bool, report_geo=Bool}

```


