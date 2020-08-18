<template>
 <div id="app">
  <v-app id="inspire">

    <div class="app">
		<div class="lists">
			<div class="list">
				<div class="list-item" draggable="true">activation</div>
				<div class="list-item" draggable="true">layer</div>  
				<div class="list-item" draggable="true">conv</div>
			</div>
			<div id="arch" class="list"> </div>
		</div>
    <button @click="send" >send arch</button>
	</div>
  
  </v-app>
</div>
</template>

<script>

//import HelloWorld from './components/HelloWorld';
import axios from "axios";

export default {
  name: 'Main--old',

  data: () => ({

    component: Main,
    components: [Regression, Tabular, Image],

    list_items: document.getElementsByClassName("list-item"),
    lists: document.getElementsByClassName('list'),
    draggedItem: null,

    component_names: ["Layer", "Activation", "Optimizer", "Loss"],
    activation: null,
    activations: ["ReLU", "Leaky ReLU", "Sigmoid", "Softmax"],
    optimizer: null,
    optimizers: ["Adam", "SGD"],
    loss: null,
    losses: ["MAE", "MBE", "Cross Entropy"],
    layer: null,
    layers: ["Input", "Linear", "Hidden", "Output", "1D", "2D", "3D"],

    map: {
      Layer: ["Input", "Linear", "Hidden", "Output", "1D", "2D", "3D"],
      Activation: ["ReLU", "Leaky ReLU", "Sigmoid", "Softmax"],
      Optimizer: ["Adam", "SGD"],
      Loss:["MAE", "MBE", "Cross Entropy"]
    },
    
    tab: null,
    text: "text",
    select:null,
    name: "",
    email: "",
    items: ["item1", "item2", "item3"],
    isMouseDown: false,
    mouseOffset: {x:0, y:0}
  }),
  methods: {
    send(){
      var divs = document.getElementById("arch").childNodes
      var name = null
      var arch = []

      for (var i=0; i < divs.length; i++){
        name = divs[i].textContent
        arch.push(name)
        console.log("name ", name)
      }

      var obj = {arch: arch}
     
      axios.post("http://127.0.0.1:3000/arch", obj)
           .then(res => console.log(res))
           .catch(err => console.log(err))
    },  
    onMouseDown() {
      this.isMouseDown = true
      console.log("down")
      console.log(event)
      console.log(event.clientX); // x coordinate
      console.log(event.clientY); // y coordinate
      /*
      // pageX/Y gives the coordinates relative to the <html> element in CSS pixels.
      console.log(event.pageX); 
      console.log(event.pagey); 

      // screenX/Y gives the coordinates relative to the screen in device pixels.
      console.log(event.screenX);
      console.log(event.screenY);
      */
      /*
      this.isMouseDown = true;
      
      this.mouseOffset = {x: item.offsetLeft - e.clientX, y: item.offsetTop - e.clientY};
      
      item.style.backgroundColor = "#E57373";
      */
    },
    onMouseUp() {
      console.log("up")
      this.isMouseDown = false;
      //event.style.backgroundColor = "#F44336";
    },
    onMouseMove(e, item) {
      e.preventDefault(); ///< Stops the Default Element Bahiavor 
      if(this.isMouseDown) {
        //Move Item only when mouse is down 
        item.style.left = e.clientX + this.mouseOffset.x + "px";
        item.style.top = e.clientY + this.mouseOffset.y + "px";
        //Concatinating Numbers with Strings is Javascript gives you a String
      }
    }
  },
};
</script>