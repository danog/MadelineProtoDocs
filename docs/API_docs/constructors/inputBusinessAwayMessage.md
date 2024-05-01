---
title: "inputBusinessAwayMessage"
description: "inputBusinessAwayMessage attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputBusinessAwayMessage  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|offline\_only|[Bool](/API_docs/types/Bool.html) | Optional|
|shortcut\_id|[int](/API_docs/types/int.html) | Yes|
|schedule|[BusinessAwayMessageSchedule](/API_docs/types/BusinessAwayMessageSchedule.html) | Yes|
|recipients|[InputBusinessRecipients](/API_docs/types/InputBusinessRecipients.html) | Yes|



### Type: [InputBusinessAwayMessage](/API_docs/types/InputBusinessAwayMessage.html)


### Example:

```
$inputBusinessAwayMessage = ['_' => 'inputBusinessAwayMessage', 'offline_only' => Bool, 'shortcut_id' => int, 'schedule' => BusinessAwayMessageSchedule, 'recipients' => InputBusinessRecipients];
```  
