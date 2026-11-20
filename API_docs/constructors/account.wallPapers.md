# account.wallPapers

> Installed wallpapers

[Back to constructors index](/API_docs/constructors/index.html)



Installed [wallpapers](https://core.telegram.org/api/wallpapers)

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|hash|[long](/API_docs/types/long.html) | Yes|[Hash used for caching, for more info click here](https://core.telegram.org/api/offsets#hash-generation)|
|wallpapers|Array of [WallPaper](/API_docs/types/WallPaper.html) | Yes|[Wallpapers](https://core.telegram.org/api/wallpapers)|



### Type: [account.WallPapers](/API_docs/types/account.WallPapers.html)


### Example:

```
$account_wallPapers = ['_' => 'account.wallPapers', 'hash' => long, 'wallpapers' => [WallPaper, WallPaper]];
```
