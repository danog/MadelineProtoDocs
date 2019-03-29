---
title: messages.sentMessageLink
description: Sent message link
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
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
|pts\_count|[int](../types/int.md) | Yes|Pts count|
|links|Array of [contacts\_Link](../types/contacts_Link.md) | Yes|Links|
|seq|[int](../types/int.md) | Yes|Seq|



### Type: [messages\_SentMessage](../types/messages_SentMessage.md)


### Example:

```php
$messages_sentMessageLink = ['_' => 'messages.sentMessageLink', 'id' => int, 'date' => int, 'pts' => int, 'pts_count' => int, 'links' => [contacts_Link, contacts_Link], 'seq' => int];
```  


Or, if you're into Lua:

```lua
messages_sentMessageLink={_='messages.sentMessageLink', id=int, date=int, pts=int, pts_count=int, links={contacts_Link}, seq=int}

```


