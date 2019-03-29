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
|seq|[int](../types/int.md) | Yes|Seq|
|links|Array of [contacts\_Link](../types/contacts_Link.md) | Yes|Links|



### Type: [messages\_SentMessage](../types/messages_SentMessage.md)


### Example:

```php
$messages_sentMessageLink = ['_' => 'messages.sentMessageLink', 'id' => int, 'date' => int, 'pts' => int, 'seq' => int, 'links' => [contacts_Link, contacts_Link]];
```  


Or, if you're into Lua:

```lua
messages_sentMessageLink={_='messages.sentMessageLink', id=int, date=int, pts=int, seq=int, links={contacts_Link}}

```


