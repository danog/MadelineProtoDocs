# help.peerColors

> Contains info about multiple color palettes ».

[Back to constructors index](/API_docs/constructors/index.html)



Contains info about multiple [color palettes »](https://core.telegram.org/api/colors).

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|hash|[int](/API_docs/types/int.html) | Yes|
|colors|Array of [help.PeerColorOption](/API_docs/constructors/help.PeerColorOption.html) | Yes|Usable [color palettes](https://core.telegram.org/api/colors).|



### Type: [help.PeerColors](/API_docs/types/help.PeerColors.html)


### Example:

```
$help_peerColors = ['_' => 'help.peerColors', 'hash' => int, 'colors' => [help.PeerColorOption, help.PeerColorOption]];
```
