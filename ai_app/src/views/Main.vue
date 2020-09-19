
<template>
    <v-container>
        <v-toolbar color='' dark height="100">
      <v-toolbar-title>Image classification</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-avatar tile size="70">
        <img src="@/assets/tf.png" alt="alt">
      </v-avatar>
    </v-toolbar>

        <v-row justify="space-around">
        
        <v-col >
            <v-card to="/regression" class="mx-auto " max-width="220" >

                <v-img :src="require('../assets/regr.jpg')" width="220" height="220" ></v-img>
                <v-card-title> Regression </v-card-title>
                <v-card-text class="text--primary"> Fit model </v-card-text>

            </v-card>
        </v-col>
        <v-col>
            <v-card to="/sound" class="mx-auto" max-width="220" >

                <v-img :src="require('../assets/onde.jpg')" width="220" height="220" ></v-img>
                <v-card-title> Sound classification </v-card-title>
                <v-card-text class="text--primary"> Train a model </v-card-text>

            </v-card>
        </v-col>
        <v-col>
            <v-card to="/tabular"  class="mx-auto" max-width="220" >

                <v-img :src="require('../assets/rf.png')" width="220" height="220" ></v-img>
                <v-card-title> Tabular Data </v-card-title>
                <v-card-text class="text--primary"> Train a classifier </v-card-text>

            </v-card>
        </v-col>
        <v-col>
            <v-card to="/ImageClassification"  class="mx-auto" max-width="220"  >

                <v-img :src="require('../assets/image-clf.png')" width="220" height="220" ></v-img>
                <v-card-title> Image classification </v-card-title>
                <v-card-text class="text--primary"> Build a NN/CNN </v-card-text>

            </v-card>
        </v-col>   
        </v-row>
    </v-container>
</template>

<script>

import axios from "axios";

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
  }
};
</script>