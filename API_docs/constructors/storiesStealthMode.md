# storiesStealthMode

> Information about the current stealth mode session.

[Back to constructors index](/API_docs/constructors/index.html)



Information about the current [stealth mode](https://core.telegram.org/api/stories#stealth-mode) session.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|active\_until\_date|[int](/API_docs/types/int.html) | Optional|The date up to which stealth mode will be active.|
|cooldown\_until\_date|[int](/API_docs/types/int.html) | Optional|The date starting from which the user will be allowed to re-enable stealth mode again.|



### Type: [StoriesStealthMode](/API_docs/types/StoriesStealthMode.html)


### Example:

```
$storiesStealthMode = ['_' => 'storiesStealthMode', 'active_until_date' => int, 'cooldown_until_date' => int];
```
