---
title: pageBlockAuthorDate
description: Author and date of creation of article
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: pageBlockAuthorDate  
[Back to constructors index](index.md)



Author and date of creation of article

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|author|[RichText](../types/RichText.md) | Yes|Author name|
|published\_date|[int](../types/int.md) | Yes|Date of pubblication|



### Type: [PageBlock](../types/PageBlock.md)


### Example:

```php
$pageBlockAuthorDate = ['_' => 'pageBlockAuthorDate', 'author' => RichText, 'published_date' => int];
```  


Or, if you're into Lua:

```lua
pageBlockAuthorDate={_='pageBlockAuthorDate', author=RichText, published_date=int}

```


