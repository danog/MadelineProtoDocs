---
title: "channelAdminLogEventActionToggleGroupCallSetting"
description: "Group call settings were changed"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: channelAdminLogEventActionToggleGroupCallSetting  
[Back to constructors index](/API_docs/constructors/index.html)



Group call settings were changed

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|join\_muted|[Bool](/API_docs/types/Bool.html) | Yes|Whether all users are muted by default upon joining|



### Type: [ChannelAdminLogEventAction](/API_docs/types/ChannelAdminLogEventAction.html)


### Example:

```
$channelAdminLogEventActionToggleGroupCallSetting = ['_' => 'channelAdminLogEventActionToggleGroupCallSetting', 'join_muted' => Bool];
```  
