# textUrl

> Link

[Back to constructors index](/API_docs/constructors/index.html)



Link

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|text|[RichText](/API_docs/types/RichText.html) | Yes|Text of link|
|url|[string](/API_docs/types/string.html) | Yes|Webpage HTTP URL|
|webpage\_id|[long](/API_docs/types/long.html) | Yes|If a preview was already generated for the page, the page ID|



### Type: [RichText](/API_docs/types/RichText.html)


### Example:

```
$textUrl = ['_' => 'textUrl', 'text' => RichText, 'url' => 'string', 'webpage_id' => long];
```
