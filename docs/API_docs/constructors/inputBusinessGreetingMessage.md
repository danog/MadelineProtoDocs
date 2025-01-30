---
title: "inputBusinessGreetingMessage"
description: "Describes a Telegram Business greeting, automatically sent to new users writing to us in private for the first time, or after a certain inactivity period."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: inputBusinessGreetingMessage  
[Back to constructors index](/API_docs/constructors/index.html)



Describes a [Telegram Business greeting](https://core.telegram.org/api/business#greeting-messages), automatically sent to new users writing to us in private for the first time, or after a certain inactivity period.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|shortcut\_id|[int](/API_docs/types/int.html) | Yes|ID of a [quick reply shorcut, containing the greeting messages to send, see here » for more info](https://core.telegram.org/api/business#quick-reply-shortcuts).|
|recipients|[InputBusinessRecipients](/API_docs/types/InputBusinessRecipients.html) | Yes|Allowed recipients for the greeting messages.|
|no\_activity\_days|[int](/API_docs/types/int.html) | Yes|The number of days after which a private chat will be considered as inactive; currently, must be one of 7, 14, 21, or 28.|



### Type: [InputBusinessGreetingMessage](/API_docs/types/InputBusinessGreetingMessage.html)


### Example:

```
$inputBusinessGreetingMessage = ['_' => 'inputBusinessGreetingMessage', 'shortcut_id' => int, 'recipients' => InputBusinessRecipients, 'no_activity_days' => int];
```  
