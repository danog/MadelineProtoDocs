# channelAdminLogEventActionChangeWallpaper

> The wallpaper was changed

[Back to constructors index](/API_docs/constructors/index.html)



The [wallpaper](https://core.telegram.org/api/wallpapers) was changed

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|prev\_value|[WallPaper](/API_docs/types/WallPaper.html) | Yes|Previous wallpaper|
|new\_value|[WallPaper](/API_docs/types/WallPaper.html) | Yes|New wallpaper|



### Type: [ChannelAdminLogEventAction](/API_docs/types/ChannelAdminLogEventAction.html)


### Example:

```
$channelAdminLogEventActionChangeWallpaper = ['_' => 'channelAdminLogEventActionChangeWallpaper', 'prev_value' => WallPaper, 'new_value' => WallPaper];
```
