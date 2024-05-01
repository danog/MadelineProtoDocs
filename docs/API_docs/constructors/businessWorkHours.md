---
title: "businessWorkHours"
description: "businessWorkHours attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: businessWorkHours  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|open\_now|[Bool](/API_docs/types/Bool.html) | Optional|
|timezone\_id|[string](/API_docs/types/string.html) | Yes|
|weekly\_open|Array of [BusinessWeeklyOpen](/API_docs/types/BusinessWeeklyOpen.html) | Yes|



### Type: [BusinessWorkHours](/API_docs/types/BusinessWorkHours.html)


### Example:

```
$businessWorkHours = ['_' => 'businessWorkHours', 'open_now' => Bool, 'timezone_id' => 'string', 'weekly_open' => [BusinessWeeklyOpen, BusinessWeeklyOpen]];
```  
