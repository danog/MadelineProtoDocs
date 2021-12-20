---
title: "pageBlockDetails"
description: "A collapsible details block"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: pageBlockDetails  
[Back to constructors index](index.md)



A collapsible details block

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|open|[Bool](../types/Bool.md) | Optional|Whether the block is open by default|
|blocks|Array of [PageBlock](../types/PageBlock.md) | Yes|Block contents|
|title|[RichText](../types/RichText.md) | Yes|Always visible heading for the block|



### Type: [PageBlock](../types/PageBlock.md)


### Example:

```php
$pageBlockDetails = ['_' => 'pageBlockDetails', 'open' => Bool, 'blocks' => [PageBlock, PageBlock], 'title' => RichText];
```  


Or, if you're into Lua:

```lua
pageBlockDetails={_='pageBlockDetails', open=Bool, blocks={PageBlock}, title=RichText}

```


