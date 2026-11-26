# aiComposeTone

> aiComposeTone attributes, type and example

[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|creator|[Bool](/API_docs/types/Bool.html) | Optional|
|id|[long](/API_docs/types/long.html) | Yes|
|access\_hash|[long](/API_docs/types/long.html) | Yes|
|slug|[string](/API_docs/types/string.html) | Yes|
|title|[string](/API_docs/types/string.html) | Yes|
|emoji\_id|[long](/API_docs/types/long.html) | Optional|
|prompt|[string](/API_docs/types/string.html) | Optional|
|installs\_count|[int](/API_docs/types/int.html) | Optional|
|author\_id|[long](/API_docs/types/long.html) | Optional|
|example\_english|[AiComposeToneExample](/API_docs/types/AiComposeToneExample.html) | Optional|



### Type: [AiComposeTone](/API_docs/types/AiComposeTone.html)


### Example:

```
$aiComposeTone = ['_' => 'aiComposeTone', 'creator' => Bool, 'id' => long, 'access_hash' => long, 'slug' => 'string', 'title' => 'string', 'emoji_id' => long, 'prompt' => 'string', 'installs_count' => int, 'author_id' => long, 'example_english' => AiComposeToneExample];
```
