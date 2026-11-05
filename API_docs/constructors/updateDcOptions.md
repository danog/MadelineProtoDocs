# updateDcOptions

> Changes in the data center configuration options.

[Back to constructors index](/API_docs/constructors/index.html)



Changes in the data center configuration options.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|dc\_options|Array of [DcOption](/API_docs/types/DcOption.html) | Yes|New connection options|



### Type: [Update](/API_docs/types/Update.html)


### Example:

```
$updateDcOptions = ['_' => 'updateDcOptions', 'dc_options' => [DcOption, DcOption]];
```
