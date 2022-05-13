---
title: "searchResultsCalendarPeriod"
description: "Information about found messages sent on a specific day, used to split the messages in messages.searchResultsCalendar constructors by days."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: searchResultsCalendarPeriod  
[Back to constructors index](/API_docs/constructors/index.html)



Information about found messages sent on a specific day, used to split the `messages` in [messages.searchResultsCalendar](../constructors/messages.searchResultsCalendar.html) constructors by days.

Multiple searchResultsCalendarPeriod constructors are returned in [messages.searchResultsCalendar](../constructors/messages.searchResultsCalendar.html), each containing information about the first, last and total number of messages matching the filter that were sent on a specific day.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|date|[int](/API_docs/types/int.html) | Yes|The day this object is referring to.|
|min\_msg\_id|[int](/API_docs/types/int.html) | Yes|First message ID that was sent on this day.|
|max\_msg\_id|[int](/API_docs/types/int.html) | Yes|Last message ID that was sent on this day.|
|count|[int](/API_docs/types/int.html) | Yes|All messages that were sent on this day.|



### Type: [SearchResultsCalendarPeriod](/API_docs/types/SearchResultsCalendarPeriod.html)


### Example:

```
$searchResultsCalendarPeriod = ['_' => 'searchResultsCalendarPeriod', 'date' => int, 'min_msg_id' => int, 'max_msg_id' => int, 'count' => int];
```  
