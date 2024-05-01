---
title: "channelAdminLogEventActionChangeTitle"
description: "Channel/supergroup title was changed"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: channelAdminLogEventActionChangeTitle  
[Back to constructors index](/API_docs/constructors/index.html)



Channel/supergroup title was changed

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|prev\_value|[string](/API_docs/types/string.html) | Yes|Previous title|
|new\_value|[string](/API_docs/types/string.html) | Yes|New title|



### Type: [ChannelAdminLogEventAction](/API_docs/types/ChannelAdminLogEventAction.html)


### Example:

```
$channelAdminLogEventActionChangeTitle = ['_' => 'channelAdminLogEventActionChangeTitle', 'prev_value' => 'string', 'new_value' => 'string'];
```  
