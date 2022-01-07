---
title: "updateNewScheduledMessage"
description: "A message was added to the schedule queue of a chat"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: updateNewScheduledMessage  
[Back to constructors index](index.md)



A message was added to the [schedule queue of a chat](https://core.telegram.org/api/scheduled-messages)

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|message|[Message](../types/Message.md) | Optional|Message|



### Type: [Update](../types/Update.md)


### Example:

```php
$updateNewScheduledMessage = ['_' => 'updateNewScheduledMessage', 'message' => Message];
```  
