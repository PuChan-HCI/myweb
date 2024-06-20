let capture;
let shape;

// Load the file and create a p5.Geometry object.
function preload() {
  // shape = loadModel('./Tree/Tree.obj');
  shape = loadModel('assets/monkey.obj');
}

function setup() {

  // Set the canvas' width and height
  // using the browser's dimensions.
  createCanvas(windowWidth, windowHeight);
  describe('A tree drawn against a gray background.');

  // Capture (webcam)
  capture = createCapture(VIDEO);
  capture.size(320, 240);

}

function draw() {
  background(50);
  image(capture, windowWidth / 2 - capture.width / 2, 100);

  // Enable orbiting with the mouse.
  orbitControl();
  // Draw the shape.
  model(shape);

  // Text
  textSize(32);
  fill(255);
  textAlign(CENTER);
  fill(255,255,0)
  text("こんにちは", windowWidth/2, 50);

}

function mousePressed() {
  // if (mouseX > 0 && mouseX < width && mouseY > 0 && mouseY < height) {
  //   let fs = fullscreen();
  //   fullscreen(!fs);
  // }
}

function windowResized() {
  resizeCanvas(windowWidth, windowHeight);
}