---
title: pageBlockAuthorDate
description: Page block author date
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: pageBlockAuthorDate  
[Back to constructors index](index.md)



Page block author date

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|author|[RichText](../types/RichText.md) | Yes|Author|
|published\_date|[int](../types/int.md) | Yes|Published date|



### Type: [PageBlock](../types/PageBlock.md)


### Example:

```php
$pageBlockAuthorDate = ['_' => 'pageBlockAuthorDate', 'author' => RichText, 'published_date' => int];
```  

[PWRTelegram](https://pwrtelegram.xyz) json-encoded version:

```
{"_": "pageBlockAuthorDate", "author": RichText, "published_date": int}
```


Or, if you're into Lua:

```lua
pageBlockAuthorDate={_='pageBlockAuthorDate', author=RichText, published_date=int}

```


