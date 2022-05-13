---
title: "inputBotInlineMessageID64"
description: "Represents a sent inline message from the perspective of a bot"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputBotInlineMessageID64  
[Back to constructors index](/API_docs/constructors/index.html)



Represents a sent inline message from the perspective of a bot

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|dc\_id|[int](/API_docs/types/int.html) | Yes|DC ID to use when working with this inline message|
|owner\_id|[long](/API_docs/types/long.html) | Yes|ID of the owner of this message|
|id|[int](/API_docs/types/int.html) | Yes|ID of message|
|access\_hash|[long](/API_docs/types/long.html) | Yes|Access hash of message|



### Type: [InputBotInlineMessageID](/API_docs/types/InputBotInlineMessageID.html)


### Example:

```
$inputBotInlineMessageID64 = ['_' => 'inputBotInlineMessageID64', 'dc_id' => int, 'owner_id' => long, 'id' => int, 'access_hash' => long];
```  
