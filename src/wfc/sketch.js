class Tile {
  constructor(img) {
    this.img = img;
  }
}

const BLANK = 0b0;
const UP = 0b1101;
const RIGHT = 0b1110;
const DOWN = 0b0111;
const LEFT = 0b1011;
const UP_MASK = 0b1000;
const RIGHT_MASK = 0b0100;
const DOWN_MASK = 0b0010;
const LEFT_MASK = 0b0001;

let tiles = [];
let dim = 10;
let tile_size;
let grid;

class Grid {
  grid;
  tile_size;
  constructor(dim) {
    this.dim = dim;
    tile_size = width / dim;
    this.init();
  }

  init() {
    this.grid = Array.from(Array(this.dim), () => new Array(this.dim));
    for (let x = 0; x < dim; x++) {
      for (let y = 0; y < dim; y++) {
        this.grid[x][y] = {
          pos: createVector(x, y),
          collapsed: false,
          options: [BLANK, UP, RIGHT, DOWN, LEFT],
        };
      }
    }
  }

  get_lowest_entropy_cell() {
    let sorted_flat_grid = this.grid
      .flat(1)
      .filter((a) => !a.collapsed)
      .sort((a, b) => {
        return a.options.length - b.options.length;
      });
    let min_entropy_elements = sorted_flat_grid.filter((a) => {
      return a.options.length == sorted_flat_grid[0].options.length;
    });
    return random(min_entropy_elements);
  }

  is_done() {
    return this.grid.flat(1).filter((a) => !a.collapsed).length == 0;
  }

  collapse() {
    let cell = this.get_lowest_entropy_cell();
    cell.collapsed = true;
    cell.options = [random(cell.options)];

    // enforce rules on adjacent cells

    // UP
    if (cell.pos.y > 0) {
      let adj_cell = this.grid[cell.pos.x][cell.pos.y - 1];
      this.rule(cell, adj_cell, UP_MASK, DOWN_MASK);
    }
    // DOWN
    if (cell.pos.y < this.dim - 1) {
      let adj_cell = this.grid[cell.pos.x][cell.pos.y + 1];
      this.rule(cell, adj_cell, DOWN_MASK, UP_MASK);
    }
    // LEFT
    if (cell.pos.x > 0) {
      let adj_cell = this.grid[cell.pos.x - 1][cell.pos.y];
      this.rule(cell, adj_cell, LEFT_MASK, RIGHT_MASK);
    }
    // RIGHT
    if (cell.pos.x < this.dim - 1) {
      let adj_cell = this.grid[cell.pos.x + 1][cell.pos.y];
      this.rule(cell, adj_cell, RIGHT_MASK, LEFT_MASK);
    }
  }

  rule(cell, adj_cell, c_mask, adj_mask) {
    let col_bit = (cell.options[0] & c_mask) > 0;
    let valid_options = [];
    for (const option of adj_cell.options) {
      let opt_bit = (option & adj_mask) > 0;
      if (col_bit == opt_bit) {
        valid_options.push(option);
      }
    }
    adj_cell.options = valid_options;
  }

  draw() {
    for (const cell of this.grid.flat(1)) {
      if (cell.collapsed) {
        image(
          tiles[cell.options[0]].img,
          cell.pos.x * tile_size,
          cell.pos.y * tile_size,
          tile_size,
          tile_size
        );
      } else {
        stroke(75);
        noFill();
        rect(
          cell.pos.x * tile_size,
          cell.pos.y * tile_size,
          tile_size,
          tile_size
        );
      }
    }
  }
}

function setup() {
  // frameRate(25);
  createCanvas(800, 800);

  // load tiles
  tiles[BLANK] = new Tile(loadImage("tiles/blank.png"));
  tiles[UP] = new Tile(loadImage("tiles/up.png"));
  tiles[RIGHT] = new Tile(loadImage("tiles/right.png"));
  tiles[DOWN] = new Tile(loadImage("tiles/down.png"));
  tiles[LEFT] = new Tile(loadImage("tiles/left.png"));

  grid = new Grid(dim);
}

function draw() {
  background(0);
  grid.collapse();
  grid.draw();
  if (grid.is_done()) {
    noLoop();
  }
}
