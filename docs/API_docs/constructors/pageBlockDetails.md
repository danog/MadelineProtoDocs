---
title: pageBlockDetails
description: Page block details
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: pageBlockDetails  
[Back to constructors index](index.md)



Page block details

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|open|[Bool](../types/Bool.md) | Optional|Open?|
|blocks|Array of [PageBlock](../types/PageBlock.md) | Yes|Blocks|
|title|[RichText](../types/RichText.md) | Yes|Title|



### Type: [PageBlock](../types/PageBlock.md)


### Example:

```php
$pageBlockDetails = ['_' => 'pageBlockDetails', 'open' => Bool, 'blocks' => [PageBlock, PageBlock], 'title' => RichText];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "pageBlockDetails", "open": Bool, "blocks": [PageBlock], "title": RichText}
```


Or, if you're into Lua:

```lua
pageBlockDetails={_='pageBlockDetails', open=Bool, blocks={PageBlock}, title=RichText}

```


