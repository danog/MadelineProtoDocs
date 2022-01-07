---
title: "messages.searchResultsCalendar"
description: "messages.searchResultsCalendar attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/messages_searchResultsCalendar.html
---
# Constructor: messages.searchResultsCalendar  
[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|inexact|[Bool](/API_docs/types/Bool.html) | Optional|
|count|[int](/API_docs/types/int.html) | Yes|
|min\_date|[int](/API_docs/types/int.html) | Yes|
|min\_msg\_id|[int](/API_docs/types/int.html) | Yes|
|offset\_id\_offset|[int](/API_docs/types/int.html) | Optional|
|periods|Array of [SearchResultsCalendarPeriod](/API_docs/types/SearchResultsCalendarPeriod.html) | Yes|
|messages|Array of [Message](/API_docs/types/Message.html) | Yes|
|chats|Array of [Chat](/API_docs/types/Chat.html) | Yes|
|users|Array of [User](/API_docs/types/User.html) | Yes|



### Type: [messages.SearchResultsCalendar](/API_docs/types/messages.SearchResultsCalendar.html)


### Example:

```php
$messages_searchResultsCalendar = ['_' => 'messages.searchResultsCalendar', 'inexact' => Bool, 'count' => int, 'min_date' => int, 'min_msg_id' => int, 'offset_id_offset' => int, 'periods' => [SearchResultsCalendarPeriod, SearchResultsCalendarPeriod], 'messages' => [Message, Message], 'chats' => [Chat, Chat], 'users' => [User, User]];
```  
