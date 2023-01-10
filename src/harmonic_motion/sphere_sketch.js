const CANVAS_SIZE = 800;

let cur_angle = 0;
let angle_offset = 0.01;
let frames;
function setup() {
  createCanvas(800, 800, WEBGL);
  frames = TWO_PI / angle_offset;
}

function draw() {
  background(0);
  noStroke();
  // ambientLight(10);
  rotateX(cur_angle * 2);
  rotateY(cur_angle);
  rotateZ(cur_angle * 2);
  directionalLight(125, 0, 125, 1, 1, 0);
  directionalLight(0, 0, 125, cos(cur_angle), -sin(cur_angle), 0);
  specularMaterial(255, 255, 255);
  push();
  cur_x = map(cos(cur_angle + PI), -1, 1, -200, 200);
  cur_y = map(sin(cur_angle), -1, 1, -200, 200);
  translate(cur_x, cur_y, cur_y);
  sphere(map(sin(cur_angle - PI), -1, 1, 50, 100));
  pop();
  push();
  cur_x = map(cos(cur_angle), -1, 1, -200, 200);
  cur_y = map(sin(cur_angle), -1, 1, -200, 200);
  translate(cur_x, cur_y, 0);
  sphere(map(sin(cur_angle), -1, 1, 50, 100));
  pop();
  push();
  cur_x = map(cos(cur_angle - HALF_PI), -1, 1, -200, 200);
  cur_y = map(sin(cur_angle - HALF_PI), -1, 1, -200, 200);
  translate(cur_x, cur_y, 0);
  sphere(map(cos(cur_angle), -1, 1, 50, 100));
  pop();
  // push();
  // cur_x = map(cos(cur_angle - HALF_PI), -1, 1, -200, 200);
  // cur_y = map(sin(cur_angle), -1, 1, -200, 200);
  // translate(cur_x, cur_y, cur_x);
  // sphere(100);
  // pop();
  cur_angle += angle_offset;
}

function keyPressed() {
  if (key == "s") {
    saveGif("test", frames, { delay: 0, units: "frames" });
  }
}
