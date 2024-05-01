---
title: "inputBotInlineMessageID"
description: "Represents a sent inline message from the perspective of a bot (legacy constructor)"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputBotInlineMessageID  
[Back to constructors index](/API_docs/constructors/index.html)



Represents a sent inline message from the perspective of a bot (legacy constructor)

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|dc\_id|[int](/API_docs/types/int.html) | Yes|DC ID to use when working with this inline message|
|id|[long](/API_docs/types/long.html) | Yes|ID of message, contains both the (32-bit, legacy) owner ID and the message ID, used only for Bot API backwards compatibility with 32-bit user ID.|
|access\_hash|[long](/API_docs/types/long.html) | Yes|Access hash of message|



### Type: [InputBotInlineMessageID](/API_docs/types/InputBotInlineMessageID.html)


### Example:

```
$inputBotInlineMessageID = ['_' => 'inputBotInlineMessageID', 'dc_id' => int, 'id' => long, 'access_hash' => long];
```  
