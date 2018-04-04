---
title: pageBlockFooter
description: pageBlockFooter attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
## Constructor: pageBlockFooter  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|text|[RichText](../types/RichText.md) | Yes|



### Type: [PageBlock](../types/PageBlock.md)


### Example:

```
$pageBlockFooter = ['_' => 'pageBlockFooter', 'text' => RichText];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "pageBlockFooter", "text": RichText}
```


Or, if you're into Lua:  


```
pageBlockFooter={_='pageBlockFooter', text=RichText}

```


