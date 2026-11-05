# updateDeleteGroupCallMessages

> updateDeleteGroupCallMessages attributes, type and example

[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|call|[InputGroupCall](/API_docs/types/InputGroupCall.html) | Yes|
|messages|Array of [int](/API_docs/types/int.html) | Yes|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updateDeleteGroupCallMessages = ['_' => 'updateDeleteGroupCallMessages', 'call' => InputGroupCall, 'messages' => [int, int]];
```
