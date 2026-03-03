---
title: "messageEntityFormattedDate"
description: "messageEntityFormattedDate attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageEntityFormattedDate  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|relative|[Bool](/API_docs/types/Bool.html) | Optional|
|short\_time|[Bool](/API_docs/types/Bool.html) | Optional|
|long\_time|[Bool](/API_docs/types/Bool.html) | Optional|
|short\_date|[Bool](/API_docs/types/Bool.html) | Optional|
|long\_date|[Bool](/API_docs/types/Bool.html) | Optional|
|day\_of\_week|[Bool](/API_docs/types/Bool.html) | Optional|
|offset|[int](/API_docs/types/int.html) | Yes|
|length|[int](/API_docs/types/int.html) | Yes|
|date|[int](/API_docs/types/int.html) | Yes|



### Type: [MessageEntity](/API_docs/types/MessageEntity.html)


### Example:

```
$messageEntityFormattedDate = ['_' => 'messageEntityFormattedDate', 'relative' => Bool, 'short_time' => Bool, 'long_time' => Bool, 'short_date' => Bool, 'long_date' => Bool, 'day_of_week' => Bool, 'offset' => int, 'length' => int, 'date' => int];
```  
