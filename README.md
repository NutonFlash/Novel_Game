# 12 Labors Of Hercules
## Interactive game for the festival in Woosong University
Important syntax:
- **Displaying Images**:
  - `image` - defines a new image
  - `show` - shows an image on a layer
  - `scene` - clears a layer, and optionally shows an image on that layer
  - `hide` - removes an image from a layer
  - [more information here](https://www.renpy.org/doc/html/displaying_images.html)
- **Transitionslink**:
  - `fade` - takes 0.5 seconds to fade to black, and then 0.5 seconds to fade to the new screen
  -  `dissolve` - takes 0.5 seconds to dissolve from the old to the new screen
  -  `pixellate` - pixellates the old scene for .5 seconds, and the new scene for another .5 seconds
  -  `move` - takes 0.5 seconds to the move images that have changed location to their new locations
  -  `moveinright, moveinleft, moveintop, moveinbottom` - these move entering images onto the screen from the appropriate side, taking 0.5 seconds to do so
  -  `moveoutright, moveoutleft, moveouttop, moveoutbottom` - these move leaving images off the screen via the appropriate side, taking 0.5 seconds to do so
  -  `ease (easeinright, easeinleft, easeintop, easeinbottom, easeoutright, easeoutleft, easeouttop, easeoutbottom)` - these are similar to the move- family of transitions, except that they use a cosine-based curve to slow down the start and end of the transition
