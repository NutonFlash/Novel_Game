# 12 Labors Of Hercules
## Interactive game for the festival in Woosong University
Important syntax:
- **label** - statement that allows the given name to be assigned to a program point; there are two kinds of labels: *global* and *local*. [More information here](https://www.renpy.org/doc/html/label.html#label-statement)
- **jump** - statement is used to transfer control to the given label; unlike call, jump doesn't allow to return to where you've jumped from. [More information here](https://www.renpy.org/doc/html/label.html#jump-statement)
- **call** - statement is used to transfer control to the given label, also pushes the next statement onto the call stack; allowing the return statement to return control to the statement following the call. [More information here](https://www.renpy.org/doc/html/label.html#call-statement)
- **menu** - statement that makes it easy to present choices to the user. [More information here](https://www.renpy.org/doc/html/menus.html)
- **return** - statement pops the top statement off of the call stack, and transfers control to it. [More information here](https://www.renpy.org/doc/html/label.html#return-statement)
- **Special Labels**:
  - `start` - by default, Ren'Py jumps to this label when the game starts
  - `quit` - if it exists, this label is called in a new context when the user quits the game
  - `after_load` - if it exists, this label is called when a game is loaded. It can be use to fix data when the game is updated
  - `splashscreen` - if it exists, this label is called when the game is first run, before showing the main menu
  - `before_main_menu` - if it exists, this label is called before the main menu. It is used in rare cases to set up the main menu, for example by starting a movie playing in the background
  - `main_menu` - if it exists, this label is called instead of the main menu
  - `after_warp` - if it is existed, this label is called after a warp but before the warped-to statement executes
  - `hide_windows` - if it exists, this label is called when the player hides the windows with the right mouse button or the H key
- **Character(params)** - creates and returns a Character object, which controls the look and feel of dialogue and narration. [More information here](https://www.renpy.org/doc/html/dialogue.html#defining-character-objects)
- **Displaying Images**:
  - `image` - defines a new image
  - `show` - shows an image on a layer
  - `scene` - clears a layer, and optionally shows an image on that layer
  - `hide` - removes an image from a layer
  - [More information here](https://www.renpy.org/doc/html/displaying_images.html)
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
- **Transforms**:
  - *Transforms can be applied to a displayable by giving the at clause to the scene and show* (`show eileen happy` **at** `right`)
  - `default` - can be redefined via `config.default_transform` to change the default placement of images shown with the show or scene statements
  - `center` - centers horizontally, and aligns to the bottom of the screen
  - `left` - aligns to the bottom-left corner of the screen
  - `offscreenleft` - places the displayable off the left side of the screen, aligned to the bottom of the screen
  - `offscreenright` - places the displayable off the left side of the screen, aligned to the bottom of the screen
  - `reset` - resets the transform (places the displayable in the top-left corner of the screen)
  - `right` - aligns to the bottom-right corner of the screen
  - `top` - centers horizontally, and aligns to the top of the screen
  - `topleft` - aligns to the top-left corner of the screen
  - `topright` - aligns to the top-right corner of the screen
  - `truecenter` - centers both horizontally and vertically
