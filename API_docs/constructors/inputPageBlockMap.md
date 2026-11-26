# inputPageBlockMap

> inputPageBlockMap attributes, type and example

[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|geo|[InputGeoPoint](/API_docs/types/InputGeoPoint.html) | Optional|
|zoom|[int](/API_docs/types/int.html) | Yes|
|w|[int](/API_docs/types/int.html) | Yes|
|h|[int](/API_docs/types/int.html) | Yes|
|caption|[PageCaption](/API_docs/types/PageCaption.html) | Yes|



### Type: [PageBlock](/API_docs/types/PageBlock.html)


### Example:

```
$inputPageBlockMap = ['_' => 'inputPageBlockMap', 'geo' => InputGeoPoint, 'zoom' => int, 'w' => int, 'h' => int, 'caption' => PageCaption];
```
