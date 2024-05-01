---
title: "phone.groupCallStreamChannels"
description: "Info about RTMP streams in a group call or livestream"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/phone_groupCallStreamChannels.html
---
# Constructor: phone.groupCallStreamChannels  
[Back to constructors index](/API_docs/constructors/index.html)



Info about RTMP streams in a group call or livestream

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|channels|Array of [GroupCallStreamChannel](/API_docs/types/GroupCallStreamChannel.html) | Yes|RTMP streams|



### Type: [phone.GroupCallStreamChannels](/API_docs/types/phone.GroupCallStreamChannels.html)


### Example:

```
$phone_groupCallStreamChannels = ['_' => 'phone.groupCallStreamChannels', 'channels' => [GroupCallStreamChannel, GroupCallStreamChannel]];
```  
