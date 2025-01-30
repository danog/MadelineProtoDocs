---
title: "businessAwayMessageScheduleCustom"
description: "Send Telegram Business away messages to users writing to us in private in the specified time span."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: businessAwayMessageScheduleCustom  
[Back to constructors index](/API_docs/constructors/index.html)



Send [Telegram Business away messages](https://core.telegram.org/api/business#away-messages) to users writing to us in private in the specified time span.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|start\_date|[int](/API_docs/types/int.html) | Yes|Start date (UNIX timestamp).|
|end\_date|[int](/API_docs/types/int.html) | Yes|End date (UNIX timestamp).|



### Type: [BusinessAwayMessageSchedule](/API_docs/types/BusinessAwayMessageSchedule.html)


### Example:

```
$businessAwayMessageScheduleCustom = ['_' => 'businessAwayMessageScheduleCustom', 'start_date' => int, 'end_date' => int];
```  
