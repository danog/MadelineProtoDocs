---
title: "reactionCount"
description: "Reactions"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: reactionCount  
[Back to constructors index](index.md)



Reactions

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|chosen|[Bool](../types/Bool.md) | Optional|Whether the current user sent this reaction|
|reaction|[string](../types/string.md) | Yes|Reaction (a UTF8 emoji)|
|count|[int](../types/int.md) | Yes|NUmber of users that reacted with this emoji|



### Type: [ReactionCount](../types/ReactionCount.md)


### Example:

```php
$reactionCount = ['_' => 'reactionCount', 'chosen' => Bool, 'reaction' => 'string', 'count' => int];
```  


Or, if you're into Lua:

```lua
reactionCount={_='reactionCount', chosen=Bool, reaction='string', count=int}

```


