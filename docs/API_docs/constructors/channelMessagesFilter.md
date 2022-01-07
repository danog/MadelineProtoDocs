---
title: "channelMessagesFilter"
description: "Filter for getting only certain types of channel messages"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: channelMessagesFilter  
[Back to constructors index](/API_docs/constructors/index.md)



Filter for getting only certain types of channel messages

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|exclude\_new\_messages|[Bool](/API_docs/types/Bool.md) | Optional|Whether to exclude new messages from the search|
|ranges|Array of [MessageRange](/API_docs/types/MessageRange.md) | Yes|A range of messages to fetch|



### Type: [ChannelMessagesFilter](/API_docs/types/ChannelMessagesFilter.md)


### Example:

```php
$channelMessagesFilter = ['_' => 'channelMessagesFilter', 'exclude_new_messages' => Bool, 'ranges' => [MessageRange, MessageRange]];
```  
