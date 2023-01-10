# Creative Coding

A collection of somewhat artistic implementations of numerous mathematical sensations and experiments.  
Inspired by [The Coding Train](https://www.youtube.com/c/TheCodingTrain) and various generative art conference talks, empowered by [p5js](https://p5js.org/) and its python counterpart [p5py](https://github.com/p5py/p5).

## Harmonic Motion

A collection of animations that spiral around the idea of periodicity.  
Heavily inspired by [beesandbombs](https://twitter.com/beesandbombs).

<img src="media/harmonic_motion/cubes.gif" alt="spinning_cube" width="400"/>
<img src="media/harmonic_motion/spheres.gif" alt="spheres" width="400"/>

## Ulam Spiral

Implementation of the classical square [Ulam Spiral](https://en.wikipedia.org/wiki/Ulam_spiral).  
Positive integers are arranged in a spiral while marking prime numbers.  
This results in a non-random pattern.

<img src="media/ulam_spiral/ulam_explanation.png" alt="ulam explanation" width="500"/>

<img src="media/ulam_spiral/ulam_viridis.png" alt="ulam viridis" width="500"/>

## Forest on fire

Simulation of a burning forest. Guided by a initial population, tree spawn and fire spawn probability.  
A fire can spread to surrounding trees and lives only for a single frame. Quite close code replication of [this video](https://www.youtube.com/watch?v=lJ2VlcI_JuY).
![forest gif](media/forest_on_fire/forest.gif)

## Style transfer

Combining the content of an image with the style of another utilizing the [Style Transfer](https://www.cv-foundation.org/openaccess/content_cvpr_2016/papers/Gatys_Image_Style_Transfer_CVPR_2016_paper.pdf) approach. Tutorial available [here](https://colab.research.google.com/drive/1rXkHKJzH9u2hs-OAqxDLNvotVxieg9S1#scrollTo=jxRrLNslsI2w)

| Content                                                                                           |  Style                                                                                                    | Result                                                                                                  |
| ------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| <img src="src/style_transfer/images/wanderer.jpeg" alt="drawing" width="100%" height="200"/>      | <img src="src/style_transfer/images/style_2.jpeg" alt="drawing" width="100%" height="200"/>               | <img src="media/style_transfer/wanderer_abstract_style_2.png" alt="drawing" width="100%" height="200"/> |
| <img src="src/style_transfer/images/friedensengel.jpeg" alt="drawing" width="100%" height="200"/> | <img src="src/style_transfer/images/oil_sea_style.jpeg" alt="drawing" width="100%" height="200"/>         | <img src="media/style_transfer/frieden_oil_ship.png" alt="drawing" width="100%" height="200"/>          |
| <img src="src/style_transfer/images/worker.jpeg" alt="drawing" width="100%" height="200"/>        | <img src="src/style_transfer/images/vangogh.jpeg" alt="drawing" width="100%" height="200"/>               | <img src="media/style_transfer/worker_vangogh.png" alt="drawing" width="100%" height="200"/>            |
| <img src="src/style_transfer/images/notre_dame.jpeg" alt="drawing" width="100%" height="200"/>    | <img src="src/style_transfer/images/blue_geometric_shapes.jpeg" alt="drawing" width="100%" height="200"/> | <img src="media/style_transfer/notre_geo.png" alt="drawing" width="100%" height="200"/>                 |

## Mandelbrot Set

Visualization of a zoom into the [Mandelbrot Set](https://en.wikipedia.org/wiki/Mandelbrot_set).  
![mandelbrot_zoom_gif](media/mandelbrot/mandelbrot_zoom.gif)

## Sierpinski Triangle (Chaos Game)

Implementation of the [Chaos game](https://en.wikipedia.org/wiki/Sierpi%C5%84ski_triangle#Chaos_game) to visualize the Sierpinski Triangle.  
![sierpinski_triangle_gif](media/sierpinski/sierpinski_triangle.gif)

## Worley Noise

Visualization of a randomized and tuned [Worley-Noise](https://de.wikipedia.org/wiki/Worley_noise) implementation.
![worley_gallery](media/worley_noise/worley_gallery.png)

## Branching

Recursive branch visualization

<p float="left">
<img src="media/branches/brokoli_2.png" width="300" height="300"/>
<img src="media/branches/brokoli_1.png" width="300" height="300"/>
</p>

## Lissajous-esk art

<img align="left" src="media/lissajous/lj_explanation.gif" width="300" height="300"/>
Depicting complex harmonic motion by highlighting axis points over time.   
Basis are multiple connected and randomized harmonic motions that use the end point of their predecessor as a starting point.
Combining interdependently randomized parameters (axis length, rotating speed, visbility, size, ...) with common matplotlib color maps yields subjectively beautiful visuals.
<div style="clear:both;"></div>

![lissajous_gallery](media/lissajous/lj_gallery_03.png)

## Maurer-Rose

Interactive implementation of the [maurer rose](https://en.wikipedia.org/wiki/Maurer_rose) that allows visualizations for random parameters.

![gallery image](media/maurer_rose/maurer_gallery.png)

## Perlin Terrain

Procedual terrain generation based on the [perlin noise](https://en.wikipedia.org/wiki/Perlin_noise).

![perlin_terrain_gif](media/perlin_terrain/perlin_terrain.gif)

## Ray Casting

Experimenting with simplistic ray casting utilizing basic [line segmentation intersection](https://en.wikipedia.org/wiki/Line%E2%80%93line_intersection) math.
![ray_cast_gif](media/ray_cast/ray_cast.gif)
