# inputMessageReadMetric

> inputMessageReadMetric attributes, type and example

[Back to constructors index](/API_docs/constructors/index.html)



### Attributes:

| Name     |    Type       | Required |
|----------|---------------|----------|
|msg\_id|[int](/API_docs/types/int.html) | Yes|
|view\_id|[long](/API_docs/types/long.html) | Yes|
|time\_in\_view\_ms|[int](/API_docs/types/int.html) | Yes|
|active\_time\_in\_view\_ms|[int](/API_docs/types/int.html) | Yes|
|height\_to\_viewport\_ratio\_permille|[int](/API_docs/types/int.html) | Yes|
|seen\_range\_ratio\_permille|[int](/API_docs/types/int.html) | Yes|



### Type: [InputMessageReadMetric](/API_docs/types/InputMessageReadMetric.html)


### Example:

```
$inputMessageReadMetric = ['_' => 'inputMessageReadMetric', 'msg_id' => int, 'view_id' => long, 'time_in_view_ms' => int, 'active_time_in_view_ms' => int, 'height_to_viewport_ratio_permille' => int, 'seen_range_ratio_permille' => int];
```
