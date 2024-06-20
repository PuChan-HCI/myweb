function setup() {
  
  // Set the canvas' width and height
  // using the browser's dimensions.
  createCanvas(windowWidth, windowHeight);
  background(0)
}

function draw() {
  background(0)
  // if (mouseIsPressed) {
  //   fill(255);
  // } else {
  //   fill(255,0,0);
  // }
  ellipse(mouseX, mouseY, 80, 80);
}

function mousePressed() {
  if (mouseX > 0 && mouseX < width && mouseY > 0 && mouseY < height) {
    let fs = fullscreen();
    fullscreen(!fs);
  }
}

function windowResized() {
  resizeCanvas(windowWidth, windowHeight);
}