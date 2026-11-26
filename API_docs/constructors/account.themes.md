# account.themes

> Installed themes

[Back to constructors index](/API_docs/constructors/index.html)



Installed themes

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|hash|[long](/API_docs/types/long.html) | Yes|[Hash used for caching, for more info click here](https://core.telegram.org/api/offsets#hash-generation)|
|themes|Array of [Theme](/API_docs/types/Theme.html) | Yes|Themes|



### Type: [account.Themes](/API_docs/types/account.Themes.html)


### Example:

```
$account_themes = ['_' => 'account.themes', 'hash' => long, 'themes' => [Theme, Theme]];
```
