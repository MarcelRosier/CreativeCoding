function setup() {
    createCanvas(800, 600)
}


let angle = 0
let radius = 50
let wave = []

function drawEpiCycles(n) {
    let x = 0;
    let y = 0;

    for (let i = 0; i < n; i++) {
        let k = 2 * i + 1
        let prevX = x
        let prevY = y
        let curRadius = radius / ((i + 1) * 2)
        // let curAngle = angle / (i * 2 + 1)
        let curAngle = 4 * PI * angle / k * PI
        noFill()
        stroke(255, 100)
        circle(prevX, prevY, curRadius * 2)
        x += cos(curAngle) * curRadius
        y += sin(curAngle) * curRadius
        stroke(255)
        line(prevX, prevY, x, y)
        // fill(255)
        // circle(x, y, 8)
    }
    wave.unshift(y)
    if (wave.length > 600) {
        wave.pop()
    }
}

function draw() {
    const N = 5;
    background(0);
    translate(radius * 2, height / 2)
    drawEpiCycles(N)
    const dt = 0.001
    angle += dt

    //draw wave
    translate(width / 4, 0)
    noFill()
    beginShape()

    for (let i = 0; i < wave.length; i++) {
        vertex(i, wave[i])
    }
    endShape()
}