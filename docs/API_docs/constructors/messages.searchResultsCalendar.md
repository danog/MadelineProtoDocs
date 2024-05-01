---
title: "messages.searchResultsCalendar"
description: "Information about found messages sent on a specific day"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/messages_searchResultsCalendar.html
---
# Constructor: messages.searchResultsCalendar  
[Back to constructors index](/API_docs/constructors/index.html)



Information about found messages sent on a specific day

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|inexact|[Bool](/API_docs/types/Bool.html) | Optional|If set, indicates that the results may be inexact|
|count|[int](/API_docs/types/int.html) | Yes|Total number of results matching query|
|min\_date|[int](/API_docs/types/int.html) | Yes|Starting timestamp of attached messages|
|min\_msg\_id|[int](/API_docs/types/int.html) | Yes|Ending timestamp of attached messages|
|offset\_id\_offset|[int](/API_docs/types/int.html) | Optional|Indicates the absolute position of `messages[0]` within the total result set with count `count`. <br>This is useful, for example, if we need to display a `progress/total` counter (like `photo 134 of 200`, for all media in a chat, we could simply use `photo ${offset_id_offset} of ${count}`.|
|periods|Array of [SearchResultsCalendarPeriod](/API_docs/types/SearchResultsCalendarPeriod.html) | Yes|Used to split the `messages` by days: multiple [SearchResultsCalendarPeriod](../types/SearchResultsCalendarPeriod.html) constructors are returned, each containing information about the first, last and total number of messages matching the filter that were sent on a specific day.  <br>This information can be easily used to split the returned `messages` by day.|
|messages|Array of [Message](/API_docs/types/Message.html) | Yes|Messages|
|chats|Array of [Chat](/API_docs/types/Chat.html) | Yes|Mentioned chats|
|users|Array of [User](/API_docs/types/User.html) | Yes|Mentioned users|



### Type: [messages.SearchResultsCalendar](/API_docs/types/messages.SearchResultsCalendar.html)


### Example:

```
$messages_searchResultsCalendar = ['_' => 'messages.searchResultsCalendar', 'inexact' => Bool, 'count' => int, 'min_date' => int, 'min_msg_id' => int, 'offset_id_offset' => int, 'periods' => [SearchResultsCalendarPeriod, SearchResultsCalendarPeriod], 'messages' => [Message, Message], 'chats' => [Chat, Chat], 'users' => [User, User]];
```  
