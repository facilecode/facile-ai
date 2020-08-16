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
  name: 'App',

  components: {
    //HelloWorld,
  },
  mounted() {
    const list_items = document.querySelectorAll('.list-item');
    const lists = document.querySelectorAll('.list');
    let draggedItem = null;

    for (let i=0; i< list_items.length; i++){
      const item = list_items[i]

      console.log("item ", item)

      item.addEventListener('dragstart', function () {
        draggedItem = item;
        setTimeout(function () {
          item.style.display = 'none';
        }, 0)
      });

      item.addEventListener('dragend', function () {
        setTimeout(function () {
          draggedItem.style.display = 'block';
          draggedItem = null;
        }, 0);
      })

      console.log("this lists ", lists, lists.length)

      for (let j = 0; j < lists.length; j ++) {
        const list = lists[j];

        list.addEventListener('dragover', function () {
          event.preventDefault();
        });
        
        list.addEventListener('dragenter', function () {
          event.preventDefault();
          this.style.backgroundColor = 'rgba(0, 0, 0, 0.2)';
        });

        list.addEventListener('dragleave', function () {
          this.style.backgroundColor = 'rgba(0, 0, 0, 0.1)';
        });

        list.addEventListener('drop', function () {
          //console.log("drop- before append", list, list.length)
          console.log("this ", this)
          console.log("dragged item", draggedItem)
          this.append(draggedItem);
          //console.log("drop- after append", list,  list.length)
          //this.style.backgroundColor = 'rgba(0, 0, 0, 0.1)';
        });
      }      
    }
  },
  data: () => ({

    list_items: document.getElementsByClassName("list-item"),
    lists: document.getElementsByClassName('list'),
    draggedItem: null,

    tab_cv:null,
    component: null,
    component_index: [0,1,2,3,4,5],
    component_titles: ["Personnel", "Adresse", "Etudes", "Expériences", "Avatar", "CV"],
    index: 0,

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

<style>
* {
	margin: 0;
	padding: 0;
	box-sizing: border-box;
}

body {
	background-color: #FFCE00;
	font-family: 'Roboto', Helvetica, sans-serif;
}

.app {
	display: flex;
	flex-flow: column;

	width: 100vw;
	height: 100vh;
}

header {
	display: flex;
	justify-content: center;
	align-items: center;
	height: 60px;
}

.lists {
	display: flex;
	flex: 1;
	width: 100%;
	overflow-x: scroll;
}

.lists .list {
	display: flex;
	flex-flow: column;
	flex: 1;

	width: 100%;
	min-width: 250px;
	max-width: 350px;
	height: 100%;
	min-height: 150px;

	background-color: rgba(0, 0, 0, 0.1);
	margin: 0 15px;
	padding: 8px;
	transition: all 0.2s linear;
}

.lists .list .list-item {
	background-color: #F3F3F3;
	border-radius: 8px;
	padding: 15px 20px;
	text-align: center;
	margin: 4px 0px;
}

</style>