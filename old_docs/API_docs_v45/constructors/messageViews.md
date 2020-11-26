---
title: messageViews
description: messageViews attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: messageViews  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|views|[int](../types/int.md) | Optional|
|forwards|[int](../types/int.md) | Optional|
|replies|[MessageReplies](../types/MessageReplies.md) | Optional|



### Type: [MessageViews](../types/MessageViews.md)


### Example:

```php
$messageViews = ['_' => 'messageViews', 'views' => int, 'forwards' => int, 'replies' => MessageReplies];
```  


Or, if you're into Lua:

```lua
messageViews={_='messageViews', views=int, forwards=int, replies=MessageReplies}

```


