
let points = [];
let num_points = 25;

function setup() {
  createCanvas(400, 400);
  noLoop()
  for (let i = 0; i < num_points; i++) {
    points.push(createVector(random(width), random(height)))
  }
}

function draw() {
  background(0);
  stroke(255)
  loadPixels()


  for (let x = 0; x < width; x++) {
    for (let y = 0; y < height; y++) {
      let distances = []
      for (let i = 0; i < points.length; i++) {
        // distances.push(v.dist(points[i]))
        distances.push(dist(x, y, points[i].x, points[i].y))
      }
      distances.sort((a, b) => a - b)
      // let r = map(distances[3], 0, width * 10 / num_points, 255, 0)
      // let g = map(distances[2], 0, width * 10 / num_points, 255, 0)
      // let b = map(distances[1], 0, width * 10 / num_points, 255, 0)
      let v = map(distances[4], 0, width * 11 / num_points, 255, 0)
      let c = color(v)
      // let c = color(distances[0])
      // let c = color(x, y, y)

      set(x, y, c)
    }
  }
  updatePixels()

  // for (let i = 0; i < num_points; i++) {
  //   stroke(200, 0, 0)
  //   circle(points[i].x, points[i].y, 10)
  // }
}


function keyPressed(event) {
  if (event.key == 's') {
    save("worley.png")
  }
}
