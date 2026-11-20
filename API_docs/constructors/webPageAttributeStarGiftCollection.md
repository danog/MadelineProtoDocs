# webPageAttributeStarGiftCollection

> Contains info about a gift collection » for a webPage preview of a gift collection » (the webPage will have a type of telegram_collection).

[Back to constructors index](/API_docs/constructors/index.html)



Contains info about a [gift collection »](https://core.telegram.org/api/gifts#gift-collections) for a [webPage](../constructors/webPage.html) preview of a [gift collection »](https://core.telegram.org/api/gifts#gift-collections) (the [webPage](../constructors/webPage.html) will have a `type` of `telegram_collection`).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|icons|Array of [Document](/API_docs/types/Document.html) | Yes|Gifts in the collection.|



### Type: [WebPageAttribute](/API_docs/types/WebPageAttribute.html)


### Example:

```
$webPageAttributeStarGiftCollection = ['_' => 'webPageAttributeStarGiftCollection', 'icons' => [Document, Document]];
```
