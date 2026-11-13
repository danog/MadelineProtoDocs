# inputRichMessageMarkdown

> inputRichMessageMarkdown attributes, type and example

[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|rtl|[Bool](/API_docs/types/Bool.html) | Optional|
|noautolink|[Bool](/API_docs/types/Bool.html) | Optional|
|markdown|[string](/API_docs/types/string.html) | Yes|
|files|Array of [InputRichFile](/API_docs/types/InputRichFile.html) | Optional|



### Type: [InputRichMessage](/API_docs/types/InputRichMessage.html)


### Example:

```
$inputRichMessageMarkdown = ['_' => 'inputRichMessageMarkdown', 'rtl' => Bool, 'noautolink' => Bool, 'markdown' => 'string', 'files' => [InputRichFile, InputRichFile]];
```
