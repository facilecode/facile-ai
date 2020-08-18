
<template>
 <div id="app">
  <v-app id="inspire">

    <v-container>
            <v-row dense>
    
            <v-col cols="12" >
                <v-card
                color='#952175'
                dark
                >

                <div class="d-flex flex-no-wrap justify-space-between">
                    <div>
                    <v-card-title
                        class="headline"
                        v-text="title"
                    ></v-card-title>
    
                    <v-card-subtitle v-text="text"></v-card-subtitle>
                    </div>
                    
                    <v-avatar
                    class="ma-3"
                    size="125"
                    tile
                    >
                    <v-img :src="require('../assets/tf.png')"></v-img>
                    
                    </v-avatar>
                </div>
                </v-card>
            </v-col>

    
    <v-row justify="space-around">
    
    <v-col >
        <v-card @click="navigate('regression')" class="mx-auto " max-width="220" >

            <v-img :src="require('../assets/regr.jpg')" width="220" height="220" ></v-img>
            <v-card-title> Regression </v-card-title>
            <v-card-text class="text--primary"> Fit model </v-card-text>

        </v-card>
    </v-col>
    <v-col>
        <v-card @click="navigate('sound')"  class="mx-auto" max-width="220" >

            <v-img :src="require('../assets/onde.jpg')" width="220" height="220" ></v-img>
            <v-card-title> Sound classification </v-card-title>
            <v-card-text class="text--primary"> Train a model </v-card-text>

        </v-card>
    </v-col>
    <v-col>
        <v-card @click="navigate('tabular')"  class="mx-auto" max-width="220" >

            <v-img :src="require('../assets/rf.png')" width="220" height="220" ></v-img>
            <v-card-title> Tabular Data </v-card-title>
            <v-card-text class="text--primary"> Train a classifier </v-card-text>

        </v-card>
    </v-col>
    <v-col>
        <v-card @click="navigate('image')"  class="mx-auto" max-width="220"  >

            <v-img :src="require('../assets/image-clf.png')" width="220" height="220" ></v-img>
            <v-card-title> Image classification </v-card-title>
            <v-card-text class="text--primary"> Build a NN/CNN </v-card-text>

        </v-card>
    </v-col>   
    </v-row>

            </v-row>
        </v-container>

  </v-app>
</div>
</template>

<script>

//import HelloWorld from './components/HelloWorld';
import axios from "axios";
import router from "../router"

export default {
  name: 'Main',

  data: () => ({

      title: "Train models, fit classifiers",
      text: "extra",
      color: "#952175"
    
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
    navigate(task){
        console.log(router)
        router.push("/Sound")
        if (task == "regression") console.log("regression")
        if (task == "sound") console.log("sound")
        if (task == "tabular") console.log("tabular")
        if (task == "image") console.log("image")
    }
  },
};
</script>