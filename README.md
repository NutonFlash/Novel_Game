# 12 Labors Of Hercules
## Interactive game for the festival in Woosong University
Important syntax:
- **Displaying Images**:
  - `image` - defines a new image
  - `show` - shows an image on a layer
  - `scene` - clears a layer, and optionally shows an image on that layer
  - `hide` - removes an image from a layer
  - [more information here](https://www.renpy.org/doc/html/displaying_images.html)
- **Transitions**:
  - *All statements below are used with `with` statement before*
  - `fade` - takes 0.5 seconds to fade to black, and then 0.5 seconds to fade to the new screen
  -  `dissolve` - takes 0.5 seconds to dissolve from the old to the new screen
  -  `pixellate` - pixellates the old scene for .5 seconds, and the new scene for another .5 seconds
  -  `move` - takes 0.5 seconds to the move images that have changed location to their new locations
  -  `moveinright, moveinleft, moveintop, moveinbottom` - these move entering images onto the screen from the appropriate side, taking 0.5 seconds to do so
  -  `moveoutright, moveoutleft, moveouttop, moveoutbottom` - these move leaving images off the screen via the appropriate side, taking 0.5 seconds to do so
  -  `ease (easeinright, easeinleft, easeintop, easeinbottom, easeoutright, easeoutleft, easeouttop, easeoutbottom)` - these are similar to the move- family of transitions, except that they use a cosine-based curve to slow down the start and end of the transition
  -  `zoomin` - this zooms in entering images, taking 0.5 seconds to do so
  -  `zoomout` - this zooms out leaving images, taking 0.5 seconds to do so
  -  `zoominout` - this zooms in entering images and zooms out leaving images, taking 0.5 seconds to do so
  -  `vpunch` - when invoked, this transition shakes the screen vertically for a quarter second
  -  `hpunch` - when invoked, this transition shakes the screen horizontally for a quarter second
  -  `blinds` - transitions the screen in a vertical blinds effect lasting 1 second
  -  `squares` - transitions the screen in a squares effect lasting 1 second
  -  `wipeleft, wiperight, wipeup, wipedown` - wipes the scene in the given direction
  -  `slideleft, slideright, slideup, slidedown` - slides the new scene in the given direction
  -  `slideawayleft, slideawayright, slideawayup, slideawaydown` - slides the old scene in the given direction
  -  `pushright, pushleft, pushup, pushdown` - these use the new scene to slide the old scene out the named side
  -  `irisin` - use a rectangular iris to display the new screen, or hide the old screen
