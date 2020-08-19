<template>
  <div>
    <v-row justify="space-around">
        
      </v-row>
  
      <v-item-group
        v-model="selected"
      >
        <v-container class="pa-0">
          <v-row>
            <v-col
              v-for="model  in models"
              :key="model"
              cols="12"
              md="2"
            >
              <v-item v-slot:default="{ active, toggle }">
                <v-card
                  v-if="type === 'cards'"
                  :color="active ? 'green' : 'grey' "
                  class="d-flex align-center"
                  dark
                  height="50"
                  @click="toggle"
                >
                  <v-scroll-y-transition-group>
                    <div
                      class="display-0.2 flex-grow-1 text-center"
                    >
                      {{model.name}}
                    </div>
                    <!--<div>
                      <v-icon>mdi-information</v-icon>
                    </div>-->
                  </v-scroll-y-transition-group>
                </v-card>
                <v-img
                  v-else
                  src="https://picsum.photos/id/237/200/300"
                  height="150"
                  class="text-right pa-2"
                  @click="toggle"
                >
                  <v-btn
                    icon
                    dark
                  >
                    <v-icon>
                      {{ active ? 'mdi-information' : 'mdi-heart-outline' }}
                    </v-icon>
                  </v-btn>
                </v-img>
              </v-item>
            </v-col>
          </v-row>
        </v-container>
      </v-item-group>
  </div>
</template>

<script>
// @ is an alias to /src

export default {
  name: 'Regression',

  data: () => ({
    mandatory: false,
    multiple: false,
    selected: null,
    types: ["cardes", "images"],
    type: "cards",
    knn: {name: "KNN", n:5, depth: 2},
    rf: {name: "Random Forest", n:10, depth: 10},
    models: [ 
      {name: "KNN", n:5, depth: 2}, 
      {name: "Random Forest", n:10, depth: 10},
      {name: "Adaboost", n:5, depth: 2}, 
      {name: "Extra tree", n:10, depth: 10},
      {name: "Gradient boost", n:10, depth: 10},
      {name: "Decision tree", n:10, depth: 10}
    ]
    }),
    watch: {
    multiple (val) {
      this.selected = (val)
        ? this.selected >= 0 ? [this.selected] : []
        : this.selected.pop()
    },
    methods: {
      toggle(){
        console.log("ok")
      }
    },
  },
}
</script>