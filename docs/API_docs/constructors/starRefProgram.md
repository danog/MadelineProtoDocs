---
title: "starRefProgram"
description: "starRefProgram attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: starRefProgram  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|bot\_id|[long](/API_docs/types/long.html) | Yes|
|commission\_permille|[int](/API_docs/types/int.html) | Yes|
|duration\_months|[int](/API_docs/types/int.html) | Optional|
|end\_date|[int](/API_docs/types/int.html) | Optional|
|daily\_revenue\_per\_user|[StarsAmount](/API_docs/types/StarsAmount.html) | Optional|



### Type: [StarRefProgram](/API_docs/types/StarRefProgram.html)


### Example:

```
$starRefProgram = ['_' => 'starRefProgram', 'bot_id' => long, 'commission_permille' => int, 'duration_months' => int, 'end_date' => int, 'daily_revenue_per_user' => StarsAmount];
```  
