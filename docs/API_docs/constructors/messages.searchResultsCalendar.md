---
title: "messages.searchResultsCalendar"
description: "messages.searchResultsCalendar attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/messages_searchResultsCalendar.html
---
# Constructor: messages.searchResultsCalendar  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|inexact|[Bool](../types/Bool.md) | Optional|
|count|[int](../types/int.md) | Yes|
|min\_date|[int](../types/int.md) | Yes|
|min\_msg\_id|[int](../types/int.md) | Yes|
|offset\_id\_offset|[int](../types/int.md) | Optional|
|periods|Array of [SearchResultsCalendarPeriod](../types/SearchResultsCalendarPeriod.md) | Yes|
|messages|Array of [Message](../types/Message.md) | Yes|
|chats|Array of [Chat](../types/Chat.md) | Yes|
|users|Array of [User](../types/User.md) | Yes|



### Type: [messages.SearchResultsCalendar](../types/messages.SearchResultsCalendar.md)


### Example:

```php
$messages_searchResultsCalendar = ['_' => 'messages.searchResultsCalendar', 'inexact' => Bool, 'count' => int, 'min_date' => int, 'min_msg_id' => int, 'offset_id_offset' => int, 'periods' => [SearchResultsCalendarPeriod, SearchResultsCalendarPeriod], 'messages' => [Message, Message], 'chats' => [Chat, Chat], 'users' => [User, User]];
```  
