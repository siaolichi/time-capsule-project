<template>
  <div id="bg-3d"></div>
</template>
<script>
import * as THREE from "three";
import { OBJLoader, MTLLoader } from "three-obj-mtl-loader";
export default {
  name: "Three",
  data() {
    return {
      camera: null,
      scene: null,
      renderer: null,
      object: null,
      object2: null,
      object3: null,
      group1: null,
      group2: null,
      group3: null,
      ADD: 0.01,
      rayCast: null,
      mouse: null,
      intersects: null
    };
  },
  methods: {
    mouseInit() {
      const vm = this;

      document.addEventListener("click", vm.onMouseClick, false);
      document.addEventListener("mousemove", vm.onMouseMove);
      vm.rayCast = new THREE.Raycaster();
      vm.mouse = new THREE.Vector2();
      vm.mouse.x = vm.mouse.y = -1;
      vm.mouse.z = 1;
    },
    onMouseClick: function(e) {
      const vm = this;
      if (document.getElementsByTagName("canvas")[0] != undefined) {
        vm.mouse.x =
          ((e.clientX - document.getElementsByTagName("canvas")[0].offsetLeft) /
            document.getElementsByTagName("canvas")[0].offsetWidth) *
            2 -
          1;
        vm.mouse.y =
          -(
            (e.clientY - document.getElementsByTagName("canvas")[0].offsetTop) /
            document.getElementsByTagName("canvas")[0].offsetHeight
          ) *
            2 +
          1;
        vm.rayCast.setFromCamera(vm.mouse, vm.camera);
        vm.intersects.forEach(obj => {
          console.log(obj.object.parent.name);
          let element = obj.object.parent.name;
          vm.$router.push("/capsules/" + element);
        });
      }
      // console.log(`${vm.mouse.x}, ${vm.mouse.y}`);
    },
    onMouseMove: function(e) {
      const vm = this;
      if (document.getElementsByTagName("canvas")[0] != undefined) {
        vm.mouse.x =
          ((e.clientX - document.getElementsByTagName("canvas")[0].offsetLeft) /
            document.getElementsByTagName("canvas")[0].offsetWidth) *
            2 -
          1;
        vm.mouse.y =
          -(
            (e.clientY - document.getElementsByTagName("canvas")[0].offsetTop) /
            document.getElementsByTagName("canvas")[0].offsetHeight
          ) *
            2 +
          1;
        vm.rayCast.setFromCamera(vm.mouse, vm.camera);
      }
    },
    init: function() {
      const vm = this;
      // 1. create the scene
      vm.scene = new THREE.Scene();
      vm.scene.background = new THREE.Color(0xffffff);

      // 2. create an locate the camera
      vm.camera = new THREE.PerspectiveCamera(
        30,
        window.innerWidth / window.innerHeight,
        1,
        1000
      );
      vm.camera.position.z = 200;

      //3. create and locate the objects on the scene

      new MTLLoader()
        .setPath("./")
        .load("Hibernation_Capsule.mtl", async materials => {
          await materials.preload();
          new OBJLoader()
            .setMaterials(materials)
            .setPath("./")
            .load("/Hibernation Capsule.obj", obj => {
              obj.scale.multiplyScalar(0.05);
              obj.name = "capsule1";
              obj.position.set(-50, 0, 0);
              vm.object = obj;
              vm.scene.add(obj);
            });
        });
      new MTLLoader().setPath("./").load("capsule.mtl", async materials => {
        await materials.preload();
        new OBJLoader()
          .setMaterials(materials)
          .setPath("./")
          .load("/capsule.obj", obj => {
            obj.scale.multiplyScalar(500);
            obj.rotation.y = 2;
            obj.name = "capsule2";
            vm.object2 = obj;
            vm.scene.add(obj);
          });
      });

      new MTLLoader().setPath("./").load("capsule.mtl", async materials => {
        await materials.preload();
        new OBJLoader()
          .setMaterials(materials)
          .setPath("./")
          .load("/capsule.obj", obj => {
            obj.scale.multiplyScalar(500);
            obj.position.set(50, 0, 0);
            obj.name = "capsule3";
            obj.rotation.y = 1;
            vm.object3 = obj;
            vm.scene.add(obj);
          });
      });
      var loader = new THREE.FontLoader();
      loader.load(
        "https://raw.githubusercontent.com/mrdoob/three.js/master/examples/fonts/helvetiker_regular.typeface.json",
        function(font) {
          let geometry = new THREE.TextGeometry("July 18th 2018", {
            font: font,
            size: 1.5,
            height: 0.2
          });
          let material = new THREE.MeshBasicMaterial({ color: 0x000000 });
          let text1 = new THREE.Mesh(geometry, material);
          text1.position.set(-46, 0, 50);
          text1.name = "July 18th 2018";
          vm.scene.add(text1);
          geometry = new THREE.TextGeometry("Dec 24th 2018", {
            font: font,
            size: 1.5,
            height: 0.2
          });
          let text2 = new THREE.Mesh(geometry, material);
          text2.position.set(-8, 0, 50);
          text2.name = "Dec 24th 2018";
          vm.scene.add(text2);
          geometry = new THREE.TextGeometry("Jan 12nd 2019", {
            font: font,
            size: 1.5,
            height: 0.2
          });
          let text3 = new THREE.Mesh(geometry, material);
          text3.position.set(30, 0, 50);
          text3.name = "Jan 12nd 2019";
          vm.scene.add(text3);
        }
      );

      let light1 = new THREE.DirectionalLight(0xffffff, 1.0);
      light1.position.set(1000, 1000, 1000);
      vm.scene.add(light1);

      let light2 = new THREE.HemisphereLight(0x99ff99, 0x9999ff);
      vm.scene.add(light2);

      // 4. create the renderer

      vm.renderer = new THREE.WebGLRenderer();
      vm.renderer.setSize(window.innerWidth, window.innerHeight);
      document.getElementById("bg-3d").appendChild(vm.renderer.domElement);
    },
    mainLoop: function() {
      const vm = this;
      vm.renderer.render(vm.scene, vm.camera);
      vm.intersects = vm.rayCast.intersectObjects(vm.scene.children, true);
      requestAnimationFrame(vm.mainLoop);
      if (vm.object != null) vm.object.rotation.y += vm.ADD;
      if (vm.object2 != null) vm.object2.rotation.y += vm.ADD;
      if (vm.object3 != null) vm.object3.rotation.y += vm.ADD;
    }
  },
  async mounted() {
    const vm = this;
    await this.init();
    await this.mouseInit();
    await this.mainLoop();
    window.addEventListener(
      "resize",
      function() {
        vm.camera.aspect = window.innerWidth / window.innerHeight;
        vm.camera.updateProjectionMatrix();
        vm.renderer.setSize(window.innerWidth, window.innerHeight);
      },
      false
    );
  }
};
</script>

<style scoped>
canvas {
  z-index: -1;
  width: 100%;
  height: 60vh;
  top: 0px;
  left: 0px;
  border: none;
}
</style>
