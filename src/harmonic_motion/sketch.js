const CANVAS_SIZE = 800;
const MAX_HEIGHT = 400;
const BAR_GROWTH_FACTOR = 1.005;
const FRAME_RATE = 30;
const ACCENT_COLOR = (3, 196, 161);

let bar_width = 40;
let cur_angle = 0;
let angle_offset = 0.03;
let max_dist_from_center;
let is_shrinking = false;
let frames;

function setup() {
  // noLoop()
  // frameRate(FRAME_RATE);
  // smooth();
  // noLoop()
  createCanvas(800, 800, WEBGL);

  max_dist_from_center = dist(0, 0, CANVAS_SIZE, CANVAS_SIZE);
  frames = TWO_PI / angle_offset;
  console.log(frames);
}

function draw() {
  background(0);

  // camera & orientation
  // ortho(-width, width, height, -height, 0, 2000);
  ortho(
    -CANVAS_SIZE + 220,
    CANVAS_SIZE - 220,
    CANVAS_SIZE - 220,
    -CANVAS_SIZE + 220,
    0,
    2000
  );
  rotateX(PI / 6);
  rotateY(PI / 8);

  // lighting
  let light_pos = createVector(1, -1, -1);
  // ambientLight(60);
  push();

  translate(light_pos);
  box(20);
  pop();
  directionalLight(255, 0, 255, light_pos);
  // stroke(255);
  // rotateX(PI / 6 + cur_angle / 10);
  rotateY(PI / 8 + cur_angle);
  specularMaterial(3, 196, 161);
  let bar_spacing = bar_width / 4;
  for (let z = -width / 2; z < width / 2; z += bar_width) {
    for (let x = -width / 2; x < width / 2; x += bar_width) {
      push();
      let distance = dist(0, 0, x, z);
      let offset = map(distance, 0, max_dist_from_center, -2 * TWO_PI, TWO_PI);
      cur_height = -map(sin(cur_angle + offset), -1, 1, 10, MAX_HEIGHT);
      translate(x, 0, z);
      box(bar_width - bar_spacing, cur_height, bar_width - bar_spacing); //, cur_height, 10);
      pop();
    }
  }
  cur_angle -= angle_offset;

  if (is_shrinking) {
    bar_width /= BAR_GROWTH_FACTOR;
    is_shrinking = bar_width > 10;
  }
}

function keyPressed() {
  if (key == "s") {
    saveGif("test", frames, { delay: 0, units: "frames" });
  }
}
