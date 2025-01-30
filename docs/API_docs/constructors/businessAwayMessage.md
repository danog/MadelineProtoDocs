---
title: "businessAwayMessage"
description: "Describes a Telegram Business away message, automatically sent to users writing to us when we're offline, during closing hours, while we're on vacation, or in some other custom time period when we cannot immediately answer to the user."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: businessAwayMessage  
[Back to constructors index](/API_docs/constructors/index.html)



Describes a [Telegram Business away message](https://core.telegram.org/api/business#away-messages), automatically sent to users writing to us when we're offline, during closing hours, while we're on vacation, or in some other custom time period when we cannot immediately answer to the user.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|offline\_only|[Bool](/API_docs/types/Bool.html) | Optional|If set, the messages will not be sent if the account was online in the last 10 minutes.|
|shortcut\_id|[int](/API_docs/types/int.html) | Yes|ID of a [quick reply shorcut, containing the away messages to send, see here » for more info](https://core.telegram.org/api/business#quick-reply-shortcuts).|
|schedule|[BusinessAwayMessageSchedule](/API_docs/types/BusinessAwayMessageSchedule.html) | Yes|Specifies when should the away messages be sent.|
|recipients|[BusinessRecipients](/API_docs/types/BusinessRecipients.html) | Yes|Allowed recipients for the away messages.|



### Type: [BusinessAwayMessage](/API_docs/types/BusinessAwayMessage.html)


### Example:

```
$businessAwayMessage = ['_' => 'businessAwayMessage', 'offline_only' => Bool, 'shortcut_id' => int, 'schedule' => BusinessAwayMessageSchedule, 'recipients' => BusinessRecipients];
```  
