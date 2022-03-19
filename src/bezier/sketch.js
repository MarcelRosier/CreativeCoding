
let points = []
function setup() {
  createCanvas(600, 400);
  points.push(createVector(random(0, width), random(0, height)))
  points.push(createVector(random(0, width), random(0, height)))
  points.push(createVector(random(0, width), random(0, height)))
  points.push(createVector(random(0, width), random(0, height)))
}

function draw() {
  background(0);
  stroke(255)
  noFill()
  let [p1, p2, p3, p4] = points
  for (let p of points) {
    circle(p.x, p.y, 8)
  }

  // show lerps
  for (let i = 1; i < points.length; i++) {
    stroke(255, 100)
    line(points[i - 1].x, points[i - 1].y, points[i].x, points[i].y)
  }
  stroke(255)
  bezier(p1.x, p1.y, p2.x, p2.y, p3.x, p3.y, p4.x, p4.y)

}
function customBezier(p1, p2, p3, p4) {
  lerp(p1, p2)
}

function checkPointMouseCol() {
  const mouseBoundSize = 5
  for (let p of points) {
    let relX = p.x + mouseBoundSize - mouseX
    let relY = p.y + mouseBoundSize - mouseY
    if (relX >= 0 && relX <= 2 * mouseBoundSize && relY >= 0 && relY <= 2 * mouseBoundSize) {
      // intersects
      p.x = mouseX
      p.y = mouseY
      break
    }
  }
}

function mouseDragged(event) {
  checkPointMouseCol()
} 
