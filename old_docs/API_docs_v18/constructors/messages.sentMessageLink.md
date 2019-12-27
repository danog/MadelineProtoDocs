---
title: messages.sentMessageLink
description: Sent message link
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
redirect_from: /API_docs/constructors/messages_sentMessageLink.html
---
# Constructor: messages.sentMessageLink  
[Back to constructors index](index.md)



Sent message link

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[int](../types/int.md) | Yes|ID|
|date|[int](../types/int.md) | Yes|Date|
|pts|[int](../types/int.md) | Yes|Pts|
|seq|[int](../types/int.md) | Yes|Seq|
|links|Array of [contacts.Link](../constructors/contacts.Link.md) | Yes|Links|



### Type: [messages.SentMessage](../types/messages.SentMessage.md)


### Example:

```php
$messages.sentMessageLink = ['_' => 'messages.sentMessageLink', 'id' => int, 'date' => int, 'pts' => int, 'seq' => int, 'links' => [contacts.Link, contacts.Link]];
```  


Or, if you're into Lua:

```lua
messages.sentMessageLink={_='messages.sentMessageLink', id=int, date=int, pts=int, seq=int, links={contacts.Link}}

```


