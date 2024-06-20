let angle = 0;
let monkey;

function preload() {
    monkey = loadModel('monkey.obj');
}

function setup() {
    createCanvas(400, 300, WEBGL);
    angleMode(DEGREES);
}

function draw() {
    background(100);
    orbitControl();
    // ページクリックでライト、マテリアルの有無を切り替え
    if (isLightMaterialOn) {
        noStroke();
        ambientLight(200);
        directionalLight(255, 255, 255, 1, 1, 0);
        ambientMaterial(111, 67, 53)
        specularMaterial(111, 67, 53);
    }
    else {
        noLights();
        fill(255);
        stroke(1);
    }

    // monkey
    push();
    translate(-100, 0, 0);
    // 適度なサイズに拡大
    scale(40);
    // そのままでは逆さなので上下を逆にする
    rotateZ(180);
    rotateY(angle * 1.3);

    
    // サルを描画
    model(monkey);
    pop();

    angle += 1;
}

let isLightMaterialOn = true;

function mousePressed() {
    isLightMaterialOn = !isLightMaterialOn
}