---
title: dialogFilter
description: dialogFilter attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: dialogFilter  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|contacts|[Bool](../types/Bool.md) | Optional|
|non\_contacts|[Bool](../types/Bool.md) | Optional|
|groups|[Bool](../types/Bool.md) | Optional|
|broadcasts|[Bool](../types/Bool.md) | Optional|
|bots|[Bool](../types/Bool.md) | Optional|
|exclude\_muted|[Bool](../types/Bool.md) | Optional|
|exclude\_read|[Bool](../types/Bool.md) | Optional|
|exclude\_archived|[Bool](../types/Bool.md) | Optional|
|id|[int](../types/int.md) | Yes|
|title|[string](../types/string.md) | Yes|
|emoticon|[string](../types/string.md) | Optional|
|pinned\_peers|Array of [InputPeer](../types/InputPeer.md) | Yes|
|include\_peers|Array of [InputPeer](../types/InputPeer.md) | Yes|
|exclude\_peers|Array of [InputPeer](../types/InputPeer.md) | Yes|



### Type: [DialogFilter](../types/DialogFilter.md)


### Example:

```php
$dialogFilter = ['_' => 'dialogFilter', 'contacts' => Bool, 'non_contacts' => Bool, 'groups' => Bool, 'broadcasts' => Bool, 'bots' => Bool, 'exclude_muted' => Bool, 'exclude_read' => Bool, 'exclude_archived' => Bool, 'id' => int, 'title' => 'string', 'emoticon' => 'string', 'pinned_peers' => [InputPeer, InputPeer], 'include_peers' => [InputPeer, InputPeer], 'exclude_peers' => [InputPeer, InputPeer]];
```  


Or, if you're into Lua:

```lua
dialogFilter={_='dialogFilter', contacts=Bool, non_contacts=Bool, groups=Bool, broadcasts=Bool, bots=Bool, exclude_muted=Bool, exclude_read=Bool, exclude_archived=Bool, id=int, title='string', emoticon='string', pinned_peers={InputPeer}, include_peers={InputPeer}, exclude_peers={InputPeer}}

```


