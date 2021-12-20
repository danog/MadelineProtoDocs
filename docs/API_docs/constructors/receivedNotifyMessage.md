---
title: "receivedNotifyMessage"
description: "Message ID, for which PUSH-notifications were cancelled."
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: receivedNotifyMessage  
[Back to constructors index](index.md)



Message ID, for which PUSH-notifications were cancelled.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|id|[int](../types/int.md) | Yes|Message ID, for which PUSH-notifications were canceled|



### Type: [ReceivedNotifyMessage](../types/ReceivedNotifyMessage.md)


### Example:

```php
$receivedNotifyMessage = ['_' => 'receivedNotifyMessage', 'id' => int];
```  


Or, if you're into Lua:

```lua
receivedNotifyMessage={_='receivedNotifyMessage', id=int}

```


