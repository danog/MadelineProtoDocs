# messages.savedReactionTags

> List of reaction tag » names assigned by the user.

[Back to constructors index](/API_docs/constructors/index.html)



List of [reaction tag »](https://core.telegram.org/api/saved-messages#tags) names assigned by the user.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|tags|Array of [SavedReactionTag](/API_docs/types/SavedReactionTag.html) | Yes|Saved reaction tags.|
|hash|[long](/API_docs/types/long.html) | Yes|[Hash used for caching, for more info click here](https://core.telegram.org/api/offsets#hash-generation). Can also be manually regenerated, if needed, using the [custom algorithm specified here »](https://core.telegram.org/api/saved-messages#tags).|



### Type: [messages.SavedReactionTags](/API_docs/types/messages.SavedReactionTags.html)


### Example:

```
$messages_savedReactionTags = ['_' => 'messages.savedReactionTags', 'tags' => [SavedReactionTag, SavedReactionTag], 'hash' => long];
```
