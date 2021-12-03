---
title: groupCallParticipantVideoSourceGroup
description: groupCallParticipantVideoSourceGroup attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: groupCallParticipantVideoSourceGroup  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|semantics|[string](../types/string.md) | Yes|
|sources|Array of [int](../types/int.md) | Yes|



### Type: [GroupCallParticipantVideoSourceGroup](../types/GroupCallParticipantVideoSourceGroup.md)


### Example:

```php
$groupCallParticipantVideoSourceGroup = ['_' => 'groupCallParticipantVideoSourceGroup', 'semantics' => 'string', 'sources' => [int, int]];
```  


Or, if you're into Lua:

```lua
groupCallParticipantVideoSourceGroup={_='groupCallParticipantVideoSourceGroup', semantics='string', sources={int}}

```


