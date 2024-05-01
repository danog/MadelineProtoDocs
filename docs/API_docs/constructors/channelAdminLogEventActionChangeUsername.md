---
title: "channelAdminLogEventActionChangeUsername"
description: "Channel/supergroup username was changed"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: channelAdminLogEventActionChangeUsername  
[Back to constructors index](/API_docs/constructors/index.html)



Channel/supergroup username was changed

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|prev\_value|[string](/API_docs/types/string.html) | Yes|Old username|
|new\_value|[string](/API_docs/types/string.html) | Yes|New username|



### Type: [ChannelAdminLogEventAction](/API_docs/types/ChannelAdminLogEventAction.html)


### Example:

```
$channelAdminLogEventActionChangeUsername = ['_' => 'channelAdminLogEventActionChangeUsername', 'prev_value' => 'string', 'new_value' => 'string'];
```  
