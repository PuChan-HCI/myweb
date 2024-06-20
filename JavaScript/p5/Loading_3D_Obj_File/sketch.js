var teapot;

function preload() {
  teapot = loadModel("teapot.obj");
}

function setup() {
  createCanvas(400, 400, WEBGL);
  background(0);
  noStroke();
}

function draw() {
  background(0);
  ambientLight(255, 0, 0);
  directionalLight(200, 200, 0, 0, 1);
  rotateX(frameCount * 0.01);
  model(teapot);
  
}