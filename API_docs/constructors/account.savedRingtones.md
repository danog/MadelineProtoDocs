# account.savedRingtones

> A list of saved notification sounds

[Back to constructors index](/API_docs/constructors/index.html)



A list of saved notification sounds

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|hash|[long](/API_docs/types/long.html) | Yes|[Hash used for caching, for more info click here](https://core.telegram.org/api/offsets#hash-generation)|
|ringtones|Array of [Document](/API_docs/types/Document.html) | Yes|Saved notification sounds|



### Type: [account.SavedRingtones](/API_docs/types/account.SavedRingtones.html)


### Example:

```
$account_savedRingtones = ['_' => 'account.savedRingtones', 'hash' => long, 'ringtones' => [Document, Document]];
```
