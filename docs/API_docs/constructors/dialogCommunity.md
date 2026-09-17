---
title: "dialogCommunity"
description: "dialogCommunity attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: dialogCommunity  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|pinned|[Bool](/API_docs/types/Bool.html) | Optional|
|community\_id|[long](/API_docs/types/long.html) | Yes|
|notify\_settings|[PeerNotifySettings](/API_docs/types/PeerNotifySettings.html) | Yes|



### Type: [Dialog](/API_docs/types/Dialog.html)


### Example:

```
$dialogCommunity = ['_' => 'dialogCommunity', 'pinned' => Bool, 'community_id' => long, 'notify_settings' => PeerNotifySettings];
```  
