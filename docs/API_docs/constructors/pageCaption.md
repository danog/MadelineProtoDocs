---
title: "pageCaption"
description: "Page caption"
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: pageCaption  
[Back to constructors index](index.md)



Page caption

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|text|[RichText](../types/RichText.md) | Yes|Caption|
|credit|[RichText](../types/RichText.md) | Yes|Credits|



### Type: [PageCaption](../types/PageCaption.md)


### Example:

```php
$pageCaption = ['_' => 'pageCaption', 'text' => RichText, 'credit' => RichText];
```  


Or, if you're into Lua:

```lua
pageCaption={_='pageCaption', text=RichText, credit=RichText}

```


