---
title: "starsRating"
description: "Represents the profile's star rating, see here » for more info."
nav_exclude: true
image: https://docs.madelineproto.xyz/favicons/android-chrome-256x256.png
---
# Constructor: starsRating  
[Back to constructors index](/API_docs/constructors/index.html)



Represents the profile's [star rating, see here »](https://core.telegram.org/api/stars#star-rating) for more info.

### Attributes:

| Name     |    Type       | Required | Description |
|----------|---------------|----------|-------------|
|level|[int](/API_docs/types/int.html) | Yes|The current level, may be negative.|
|current\_level\_stars|[long](/API_docs/types/long.html) | Yes|The numerical value of the rating required for the current level.|
|stars|[long](/API_docs/types/long.html) | Yes|Numerical value of the current rating.|
|next\_level\_stars|[long](/API_docs/types/long.html) | Optional|The numerical value of the rating required for the next level.|



### Type: [StarsRating](/API_docs/types/StarsRating.html)


### Example:

```
$starsRating = ['_' => 'starsRating', 'level' => int, 'current_level_stars' => long, 'stars' => long, 'next_level_stars' => long];
```  
