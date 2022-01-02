---
title: "pageBlockAnchor"
description: "Link to section within the page itself (like <a href='#target'>anchor</a>)"
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: pageBlockAnchor  
[Back to constructors index](index.md)



Link to section within the page itself (like `<a href="#target">anchor</a>`)

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|name|[string](../types/string.md) | Yes|Name of target section|



### Type: [PageBlock](../types/PageBlock.md)


### Example:

```php
$pageBlockAnchor = ['_' => 'pageBlockAnchor', 'name' => 'string'];
```  


Or, if you're into Lua:

```lua
pageBlockAnchor={_='pageBlockAnchor', name='string'}

```


