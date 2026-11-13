# peerColor

> Represents a color palette ».

[Back to constructors index](/API_docs/constructors/index.html)



Represents a [color palette »](https://core.telegram.org/api/colors).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|color|[int](/API_docs/types/int.html) | Optional|[Color palette ID, see here »](https://core.telegram.org/api/colors) for more info; if not set, the default palette should be used.|
|background\_emoji\_id|[long](/API_docs/types/long.html) | Optional|Optional [custom emoji ID](https://core.telegram.org/api/custom-emoji) used to generate the pattern.|



### Type: [PeerColor](/API_docs/types/PeerColor.html)


### Example:

```
$peerColor = ['_' => 'peerColor', 'color' => int, 'background_emoji_id' => long];
```
