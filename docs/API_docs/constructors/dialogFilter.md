---
title: "dialogFilter"
description: "Dialog filter AKA folder"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: dialogFilter  
[Back to constructors index](index.md)



Dialog filter AKA [folder](https://core.telegram.org/api/folders)

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|contacts|[Bool](../types/Bool.md) | Optional|Whether to include all contacts in this [folder](https://core.telegram.org/api/folders)|
|non\_contacts|[Bool](../types/Bool.md) | Optional|Whether to include all non-contacts in this [folder](https://core.telegram.org/api/folders)|
|groups|[Bool](../types/Bool.md) | Optional|Whether to include all groups in this [folder](https://core.telegram.org/api/folders)|
|broadcasts|[Bool](../types/Bool.md) | Optional|Whether to include all channels in this [folder](https://core.telegram.org/api/folders)|
|bots|[Bool](../types/Bool.md) | Optional|Whether to include all bots in this [folder](https://core.telegram.org/api/folders)|
|exclude\_muted|[Bool](../types/Bool.md) | Optional|Whether to exclude muted chats from this [folder](https://core.telegram.org/api/folders)|
|exclude\_read|[Bool](../types/Bool.md) | Optional|Whether to exclude read chats from this [folder](https://core.telegram.org/api/folders)|
|exclude\_archived|[Bool](../types/Bool.md) | Optional|Whether to exclude archived chats from this [folder](https://core.telegram.org/api/folders)|
|id|[int](../types/int.md) | Yes|[Folder](https://core.telegram.org/api/folders) ID|
|title|[string](../types/string.md) | Yes|[Folder](https://core.telegram.org/api/folders) name|
|emoticon|[string](../types/string.md) | Optional|[Folder](https://core.telegram.org/api/folders) emoticon|
|pinned\_peers|Array of [InputPeer](../types/InputPeer.md) | Yes|Pinned chats, [folders](https://core.telegram.org/api/folders) can have unlimited pinned chats|
|include\_peers|Array of [InputPeer](../types/InputPeer.md) | Yes|Include the following chats in this [folder](https://core.telegram.org/api/folders)|
|exclude\_peers|Array of [InputPeer](../types/InputPeer.md) | Yes|Exclude the following chats from this [folder](https://core.telegram.org/api/folders)|



### Type: [DialogFilter](../types/DialogFilter.md)


### Example:

```php
$dialogFilter = ['_' => 'dialogFilter', 'contacts' => Bool, 'non_contacts' => Bool, 'groups' => Bool, 'broadcasts' => Bool, 'bots' => Bool, 'exclude_muted' => Bool, 'exclude_read' => Bool, 'exclude_archived' => Bool, 'id' => int, 'title' => 'string', 'emoticon' => 'string', 'pinned_peers' => [InputPeer, InputPeer], 'include_peers' => [InputPeer, InputPeer], 'exclude_peers' => [InputPeer, InputPeer]];
```  


Or, if you're into Lua:

```lua
dialogFilter={_='dialogFilter', contacts=Bool, non_contacts=Bool, groups=Bool, broadcasts=Bool, bots=Bool, exclude_muted=Bool, exclude_read=Bool, exclude_archived=Bool, id=int, title='string', emoticon='string', pinned_peers={InputPeer}, include_peers={InputPeer}, exclude_peers={InputPeer}}

```


