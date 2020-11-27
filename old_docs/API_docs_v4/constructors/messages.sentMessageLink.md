---
title: messages.sentMessageLink
description: messages.sentMessageLink attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/messages_sentMessageLink.html
---
# Constructor: messages.sentMessageLink  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|id|[int](../types/int.md) | Yes|
|date|[int](../types/int.md) | Yes|
|media|[MessageMedia](../types/MessageMedia.md) | Optional|
|pts|[int](../types/int.md) | Yes|
|pts\_count|[int](../types/int.md) | Yes|
|links|Array of [contacts.Link](../constructors/contacts.Link.md) | Yes|
|seq|[int](../types/int.md) | Yes|



### Type: [messages.SentMessage](../types/messages.SentMessage.md)


### Example:

```php
$messages_sentMessageLink = ['_' => 'messages.sentMessageLink', 'id' => int, 'date' => int, 'media' => MessageMedia, 'pts' => int, 'pts_count' => int, 'links' => [contacts.Link, contacts.Link], 'seq' => int];
```  


Or, if you're into Lua:

```lua
messages_sentMessageLink={_='messages.sentMessageLink', id=int, date=int, media=MessageMedia, pts=int, pts_count=int, links={contacts.Link}, seq=int}

```


