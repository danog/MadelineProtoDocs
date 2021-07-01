---
title: messageViews
description: View, forward counter + info about replies of a specific message
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageViews  
[Back to constructors index](index.md)



View, forward counter + info about replies of a specific message

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|views|[int](../types/int.md) | Optional|Viewcount of message|
|forwards|[int](../types/int.md) | Optional|Forward count of message|
|replies|[MessageReplies](../types/MessageReplies.md) | Optional|Reply and [thread](https://core.telegram.org/api/threads) information of message|



### Type: [MessageViews](../types/MessageViews.md)


### Example:

```php
$messageViews = ['_' => 'messageViews', 'views' => int, 'forwards' => int, 'replies' => MessageReplies];
```  


Or, if you're into Lua:

```lua
messageViews={_='messageViews', views=int, forwards=int, replies=MessageReplies}

```


