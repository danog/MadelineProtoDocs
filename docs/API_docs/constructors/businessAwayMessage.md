---
title: "businessAwayMessage"
description: "businessAwayMessage attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: businessAwayMessage  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|offline\_only|[Bool](/API_docs/types/Bool.html) | Optional|
|shortcut\_id|[int](/API_docs/types/int.html) | Yes|
|schedule|[BusinessAwayMessageSchedule](/API_docs/types/BusinessAwayMessageSchedule.html) | Yes|
|recipients|[BusinessRecipients](/API_docs/types/BusinessRecipients.html) | Yes|



### Type: [BusinessAwayMessage](/API_docs/types/BusinessAwayMessage.html)


### Example:

```
$businessAwayMessage = ['_' => 'businessAwayMessage', 'offline_only' => Bool, 'shortcut_id' => int, 'schedule' => BusinessAwayMessageSchedule, 'recipients' => BusinessRecipients];
```  
