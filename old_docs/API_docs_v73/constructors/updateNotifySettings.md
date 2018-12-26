---
title: updateNotifySettings
description: Update notify settings
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateNotifySettings  
[Back to constructors index](index.md)



Update notify settings

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|peer|[NotifyPeer](../types/NotifyPeer.md) | Yes|Peer|
|notify\_settings|[PeerNotifySettings](../types/PeerNotifySettings.md) | Optional|Notify settings|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateNotifySettings = ['_' => 'updateNotifySettings', 'peer' => NotifyPeer, 'notify_settings' => PeerNotifySettings];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "updateNotifySettings", "peer": NotifyPeer, "notify_settings": PeerNotifySettings}
```


Or, if you're into Lua:

```lua
updateNotifySettings={_='updateNotifySettings', peer=NotifyPeer, notify_settings=PeerNotifySettings}

```


