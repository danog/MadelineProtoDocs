# mediaAreaStarGift

> Represents a collectible gift ».

[Back to constructors index](/API_docs/constructors/index.html)



Represents a [collectible gift »](https://core.telegram.org/api/gifts#collectible-gifts).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|coordinates|[MediaAreaCoordinates](/API_docs/types/MediaAreaCoordinates.html) | Yes|Coordinates of the media area.|
|slug|[string](/API_docs/types/string.html) | Yes|`slug` from [starGiftUnique](../constructors/starGiftUnique.html).`slug`, that can be resolved as [specified here »](https://core.telegram.org/api/gifts#sharing-and-getting-info-about-a-collectible-gift).|



### Type: [MediaArea](/API_docs/types/MediaArea.html)


### Example:

```
$mediaAreaStarGift = ['_' => 'mediaAreaStarGift', 'coordinates' => MediaAreaCoordinates, 'slug' => 'string'];
```
