---
title: "groupCallDiscarded"
description: "groupCallDiscarded attributes, type and example"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: groupCallDiscarded  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|id|[long](../types/long.md) | Yes|
|access\_hash|[long](../types/long.md) | Yes|
|duration|[int](../types/int.md) | Yes|



### Type: [GroupCall](../types/GroupCall.md)


### Example:

```php
$groupCallDiscarded = ['_' => 'groupCallDiscarded', 'id' => long, 'access_hash' => long, 'duration' => int];
```  


Or, if you're into Lua:

```lua
groupCallDiscarded={_='groupCallDiscarded', id=long, access_hash=long, duration=int}

```


