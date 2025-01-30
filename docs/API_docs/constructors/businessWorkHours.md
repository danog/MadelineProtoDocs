---
title: "businessWorkHours"
description: "Specifies a set of Telegram Business opening hours."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: businessWorkHours  
[Back to constructors index](/API_docs/constructors/index.html)



Specifies a set of [Telegram Business opening hours](https://core.telegram.org/api/business#opening-hours).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|open\_now|[Bool](/API_docs/types/Bool.html) | Optional|Ignored if set while invoking [account.updateBusinessWorkHours](../methods/account.updateBusinessWorkHours.html), only returned by the server in [userFull](../constructors/userFull.html).`business_work_hours`, indicating whether the business is currently open according to the current time and the values in `weekly_open` and `timezone`.|
|timezone\_id|[string](/API_docs/types/string.html) | Yes|An ID of one of the timezones returned by [help.getTimezonesList](../methods/help.getTimezonesList.html).  <br>  The timezone ID is contained [timezone](../constructors/timezone.html).`id`, a human-readable, localized name of the timezone is available in [timezone](../constructors/timezone.html).`name` and the [timezone](../constructors/timezone.html).`utc_offset` field contains the UTC offset in seconds, which may be displayed in hh:mm format by the client together with the human-readable name (i.e. `$name UTC -01:00`).|
|weekly\_open|Array of [BusinessWeeklyOpen](/API_docs/types/BusinessWeeklyOpen.html) | Yes|A list of time intervals (max 28) represented by [businessWeeklyOpen »](../constructors/businessWeeklyOpen.html), indicating the opening hours of their business.|



### Type: [BusinessWorkHours](/API_docs/types/BusinessWorkHours.html)


### Example:

```
$businessWorkHours = ['_' => 'businessWorkHours', 'open_now' => Bool, 'timezone_id' => 'string', 'weekly_open' => [BusinessWeeklyOpen, BusinessWeeklyOpen]];
```  
