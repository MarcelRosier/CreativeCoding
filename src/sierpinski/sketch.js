let edges;
let start_point;
let center_point;
let growth_speed = 5;
let domain_size = 800

function setup_sierpinski() {
  tri_len = 800
  tri_x = width / 10
  tri_y = height / 10
  tri_mid_y = sqrt(tri_len ** 2 - (tri_len / 2) ** 2)
  let v1 = createVector(tri_x, tri_y)
  let v2 = createVector(tri_x + tri_len, tri_y)
  let v3 = createVector(tri_x + tri_len / 2, tri_mid_y)
  edges = [v1, v2, v3]
  point(v1)
  point(v2)
  point(v3)
  start_point = createVector(tri_x + 400, tri_y + 200)
  center_point = createVector(tri_x + tri_len / 2, tri_mid_y / 2)
}

function setup_random() {
  edges = []
  nodes = Math.ceil(Math.random() * 5)
  for (let i = 0; i < nodes; i++) {
    edges.push(createVector(Math.random() * 800 + 100, Math.random() * 800 + 100))
    point(edges[i])
  }

  start_point = createVector(Math.random() * 800 + 100, Math.random() * 800 + 100)
  center_point = createVector(400, 500)
}

function setup() {
  // frameRate(1)
  // noLoop()
  createCanvas(1000, 1000);
  background(0);
  stroke(255)
  // translate to bottome left corner
  translate(0, height - height / 10)
  scale(1, -1)
  // draw triangle edge points
  strokeWeight(5)
  setup_sierpinski()
  // setup_random()



  // createStructure()
}

function get_random_index(range) {
  return Math.floor(Math.random() * range)
}

function chaos_step(last_point, edges) {
  let anchor = edges[get_random_index(edges.length)]
  let new_x = Math.min(last_point.x, anchor.x) + Math.abs(anchor.x - last_point.x) / 2
  let new_y = Math.min(last_point.y, anchor.y) + Math.abs(anchor.y - last_point.y) / 2
  return createVector(new_x, new_y)
}

function draw() {
  translate(0, height - height / 10)
  scale(1, -1)
  for (let i = 0; i < growth_speed; i++) {
    index = map(start_point.dist(center_point), domain_size, 0, 1, 0,)
    // console.log(start_point.dist(center_point))
    // console.log(index)
    let color = evaluate_cmap(index, 'magma', true)
    stroke(color)
    point(start_point)
    start_point = chaos_step(start_point, edges)
  }


  // translate(width / 2, height / 2)
  // console.log(branches)
  // for (let i = 0; i < branches.length; i++) {
  //   push()
  //   branches[i].show()
  //   pop()
  //   rotate(2 * PI / (i + 1))
  // }
}

function keyPressed(event) {
  if (event.key == 's') {
    save("test.png")
  }
}