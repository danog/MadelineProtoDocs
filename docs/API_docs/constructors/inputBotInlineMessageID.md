---
title: "inputBotInlineMessageID"
description: "Represents a sent inline message from the perspective of a bot"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputBotInlineMessageID  
[Back to constructors index](/API_docs/constructors/index.html)



Represents a sent inline message from the perspective of a bot

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|dc\_id|[int](/API_docs/types/int.html) | Yes|DC ID to use when working with this inline message|
|id|[long](/API_docs/types/long.html) | Yes|ID of message|
|access\_hash|[long](/API_docs/types/long.html) | Yes|Access hash of message|



### Type: [InputBotInlineMessageID](/API_docs/types/InputBotInlineMessageID.html)


### Example:

```php
$inputBotInlineMessageID = ['_' => 'inputBotInlineMessageID', 'dc_id' => int, 'id' => long, 'access_hash' => long];
```  
