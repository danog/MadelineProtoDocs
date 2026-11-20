# nearestDc

> Nearest data center, according to geo-ip.

[Back to constructors index](/API_docs/constructors/index.html)



Nearest data center, according to geo-ip.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|country|[string](/API_docs/types/string.html) | Yes|Country code determined by geo-ip|
|this\_dc|[int](/API_docs/types/int.html) | Yes|Number of current data center|
|nearest\_dc|[int](/API_docs/types/int.html) | Yes|Number of nearest data center|



### Type: [NearestDc](/API_docs/types/NearestDc.html)


### Example:

```
$nearestDc = ['_' => 'nearestDc', 'country' => 'string', 'this_dc' => int, 'nearest_dc' => int];
```
