class Branch {
  constructor(length, depth) {
    this.length = length;
    this.depth = depth
    if (depth >= 1) {
      this.children = []
      for (let i = 0; i < 2; i++) {
        this.children.push(new Branch(length / 1.4, int(random(depth - 2, depth - 1))));
      }

    } else {
      this.children = []
    }
  }

  show() {
    let index = map(this.depth, 0, max_depth, 0, 1)
    let color = evaluate_cmap(index, 'magma', true)
    stroke(color)
    line(0, 0, 0, this.length)
    translate(0, this.length)
    if (this.children.length < 1) {
      return
    }

    for (let i = 0; i < this.children.length; i++) {
      let angle = map(i, 0, this.children.length, PI / 6, -PI / 6)
      if (random() > 0.5) {
        angle *= -1
      }

      push()
      rotate(angle)
      this.children[i].show()
      pop()
    }
  }
}



let branches = [];
let max_depth = 20

function createStructure() {
  branches = []
  for (let i = 0; i < 100; i++) {
    branches.push(new Branch(random(40, 150), random(7, max_depth)))
  }
}

function setup() {
  // frameRate(1)
  noLoop()
  createCanvas(1000, 1000);
  createStructure()
}

function draw() {
  background(0);
  stroke(255)
  translate(width / 2, height / 2)
  console.log(branches)
  for (let i = 0; i < branches.length; i++) {
    push()
    branches[i].show()
    pop()
    rotate(2 * PI / (i + 1))
  }
}

function keyPressed(event) {
  if (event.key == 's') {
    save("test.png")
  }
}
