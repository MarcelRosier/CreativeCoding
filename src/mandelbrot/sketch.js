
let max_iterations = 2500
let divergence_threshold = 16
// let center_x = -.742013
// let center_y = .1436365
// let center_x = -1.24254013716898265806
// let center_y = 0.413238151606368892027
let center_x = -1.1539583650915322
let center_y = 0.27680486534331106
let view_size = 3
let resolution = 500
let zoom_speed = 1.15
let iteration = 0


// https://de.wikipedia.org/wiki/Mandelbrot-Menge#Definition
function setup() {
  // noLoop()
  // frameRate(1)
  // noLoop()
  createCanvas(resolution, resolution);
  background(0);
  // stroke(255)
  // translate to bottome left corner
  pixelDensity(1)

}

function mouseClicked() {
  center_x = map(mouseX, 0, width, center_x - view_size, center_x + view_size)
  center_y = map(mouseY, 0, height, center_y - view_size, center_y + view_size)
  console.log(center_x, center_y)
}

function draw() {
  view_size /= zoom_speed
  loadPixels()
  for (let x = 0; x < width; x++) {
    for (let y = 0; y < height; y++) {

      // calc mandelbrot iterations
      // f_c(z) = z^2 + c
      // (a+bi) ^2 = a^2 -b^2 + 2abi

      n = 0

      c_real = map(x, 0, width, center_x - view_size, center_x + view_size)
      c_im = map(y, 0, height, center_y - view_size, center_y + view_size)
      z_real = 0
      z_im = 0
      while (n < max_iterations) {
        // calc z squared:
        next_z_real = (z_real ** 2) - (z_im ** 2) + c_real
        next_z_im = (2 * z_real * z_im) + c_im
        z_real = next_z_real
        z_im = next_z_im

        // calc sort of magnitude
        if (z_real + z_im > divergence_threshold) {
          break
        }

        n++
      }
      // let color = map(n, 0, max_iterations, 0, 255)
      let cmap_index = map(n, 0, max_iterations, 0, 1)
      let color = evaluate_cmap(sqrt(cmap_index), 'viridis', false)
      if (n == max_iterations) {
        color = [0, 0, 0]
      }

      let index = (x + y * width) * 4
      pixels[index] = color[0];
      pixels[index + 1] = color[1];
      pixels[index + 2] = color[2];
      pixels[index + 3] = 255;
    }
  }

  updatePixels()
  save(`gif/${iteration}.jpg`)
  iteration++
}

function keyPressed(event) {
  if (event.key == 's') {
    save("test.png")
  }
}
