---
title: pageBlockTitle
description: pageBlockTitle attributes, type and example
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
## Constructor: pageBlockTitle  
[Back to constructors index](index.md)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|text|[RichText](../types/RichText.md) | Yes|



### Type: [PageBlock](../types/PageBlock.md)


### Example:

```
$pageBlockTitle = ['_' => 'pageBlockTitle', 'text' => RichText];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "pageBlockTitle", "text": RichText}
```


Or, if you're into Lua:  


```
pageBlockTitle={_='pageBlockTitle', text=RichText}

```


