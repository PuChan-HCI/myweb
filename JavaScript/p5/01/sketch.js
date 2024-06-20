let capture;

function setup() {
  
  // Set the canvas' width and height
  // using the browser's dimensions.
  createCanvas(windowWidth, windowHeight);

  // Capture (webcam)
  capture = createCapture(VIDEO);
  capture.size(320, 240);

}

function draw() {
  background(255);
  Image(capture,windowWidth/2-capture.width/2, 100);
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