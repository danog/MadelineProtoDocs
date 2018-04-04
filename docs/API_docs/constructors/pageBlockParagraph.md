---
title: pageBlockParagraph
description: A text paragraph
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: pageBlockParagraph  
[Back to constructors index](index.md)



A text paragraph

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|text|[RichText](../types/RichText.md) | Yes|Paragraph text|



### Type: [PageBlock](../types/PageBlock.md)


### Example:

```
$pageBlockParagraph = ['_' => 'pageBlockParagraph', 'text' => RichText];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "pageBlockParagraph", "text": RichText}
```


Or, if you're into Lua:  


```
pageBlockParagraph={_='pageBlockParagraph', text=RichText}

```


