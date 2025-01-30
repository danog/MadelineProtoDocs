---
title: "businessWeeklyOpen"
description: "A time interval, indicating the opening hours of a business."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: businessWeeklyOpen  
[Back to constructors index](/API_docs/constructors/index.html)



A time interval, indicating the opening hours of a business.

Note that opening hours specified by the user must be appropriately validated and transformed before uploading them to the server, as specified [here »](https://core.telegram.org/api/business#opening-hours).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|start\_minute|[int](/API_docs/types/int.html) | Yes|Start minute in minutes of the week, `0` to `7*24*60` inclusively.|
|end\_minute|[int](/API_docs/types/int.html) | Yes|End minute in minutes of the week, `1` to `8*24*60` inclusively (`8` and not `7` because this allows to specify intervals that, for example, start on `Sunday 21:00` and end on `Monday 04:00` (`6*24*60+21*60` to `7*24*60+4*60`) without passing an invalid `end_minute < start_minute`). See [here »](https://core.telegram.org/api/business#opening-hours) for more info.|



### Type: [BusinessWeeklyOpen](/API_docs/types/BusinessWeeklyOpen.html)


### Example:

```
$businessWeeklyOpen = ['_' => 'businessWeeklyOpen', 'start_minute' => int, 'end_minute' => int];
```  
