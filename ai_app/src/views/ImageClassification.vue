<template>
  <div class="home">

    <v-row>
            <v-col lg="4" cols="sm" class="pb-2">
                <v-card>
                    <v-row class="no-gutters">
                        <div class="col-auto">
                            <div class="cyan fill-height">{{ space }}</div>
                        </div>
                        <div class="col pa-3 py-4 cyan--text">
                            <h5 class="text-truncate text-uppercase">Sales</h5>
                            <h1>53</h1>
                        </div>
                    </v-row>
                </v-card>
            </v-col>
            <v-col lg="4" cols="sm" class="pb-2">
                <v-card>
                    <v-row class="no-gutters">
                        <div class="col-auto">
                            <div class="primary fill-height"></div>
                        </div>
                        <div class="col pa-3 py-4 primary--text">
                            <h5 class="text-truncate text-uppercase">Growth</h5>
                            <h1>23%</h1>
                        </div>
                    </v-row>
                </v-card>
            </v-col>
            <v-col lg="4" cols="sm" class="pb-2">
                <v-card>
                    <v-row class="no-gutters">
                        <div class="col-auto">
                            <div class="success fill-height">&nbsp;</div>
                        </div>
                        <div class="col pa-3 py-4 success--text">
                            <h5 class="text-truncate text-uppercase">Calls</h5>
                            <h1>213</h1>
                        </div>
                    </v-row>
                </v-card>
            </v-col>
        </v-row>
  
   
    <v-container>
      <v-row justify="space-around">
  
        <v-switch
          v-model="drawer"
          class="ma-2"
          label="v-model"
        ></v-switch>
  
        <v-switch
          v-model="permanent"
          class="ma-2"
          label="Permanent"
        ></v-switch>
  
        <v-switch
          v-model="miniVariant"
          class="ma-2"
          label="Mini variant"
        ></v-switch>
  
        <v-switch
          v-model="expandOnHover"
          class="ma-2"
          label="Expand on hover"
        ></v-switch>
      </v-row>
  
      <v-card
        height="800"
        class="overflow-hidden"
      >
        <v-navigation-drawer
          v-model="drawer"
          :color="color"
          :expand-on-hover="expandOnHover"
          :mini-variant="miniVariant"
          :right="right"
          permanent
          :src="bg"
          dark
        >
          <v-list
            dense
            nav
            class="py-0"
          >
            <v-list-item two-line :class="miniVariant && 'px-0'">
              <v-list-item-avatar>
                <!--<img src="https://randomuser.me/api/portraits/men/81.jpg">-->
              </v-list-item-avatar>
  
              <v-list-item-content>
                <v-list-item-title>Image Classification</v-list-item-title>
                <v-list-item-subtitle>Subtext</v-list-item-subtitle>
              </v-list-item-content>
            </v-list-item>
  
            <v-divider></v-divider>

            <v-list-item link>
              <v-list-item-icon>
                <v-icon>
                  
                </v-icon>
              </v-list-item-icon>
              <v-list-item-content>
                <v-list-item-title>
                  
                </v-list-item-title>
              </v-list-item-content>
            </v-list-item>

            <v-list-item link>
              <v-list-item-icon>
                <v-icon>
                  {{'mdi-view-dashboard'}}
                </v-icon>
              </v-list-item-icon>
              <v-list-item-content>
                <v-list-item-title>
                  Models
                </v-list-item-title>
              </v-list-item-content>
            </v-list-item>

            <v-list-item link>
              <v-list-item-icon>
                <v-icon>
                  {{'mdi-layers-triple'}}
                </v-icon>
              </v-list-item-icon>
              <v-list-item-content>
                <v-list-item-title>
                  Layers
                </v-list-item-title>
              </v-list-item-content>
            </v-list-item>

            <v-list-item link>
              <v-list-item-icon>
                <v-icon>
                  {{'mdi-chart-bell-curve'}}
                </v-icon>
              </v-list-item-icon>
              <v-list-item-content>
                <v-list-item-title>
                  Optimizers
                </v-list-item-title>
              </v-list-item-content>
            </v-list-item>

            <v-list-item link>
              <v-list-item-icon>
                <v-icon>
                  {{'mdi-function-variant'}}
                </v-icon>
              </v-list-item-icon>
              <v-list-item-content>
                <v-list-item-title>
                  Loss functions
                </v-list-item-title>
              </v-list-item-content>
            </v-list-item>

            <v-list-item link>
              <v-list-item-icon>
                <v-icon>
                  {{'mdi-tools'}}
                </v-icon>
              </v-list-item-icon>
              <v-list-item-content>
                <v-list-item-title>
                  Tools
                </v-list-item-title>
              </v-list-item-content>
            
            </v-list-item>  

          </v-list>
        </v-navigation-drawer>

        <v-card flex>
          <v-img :src="require('../assets/rf.png')" width="400" height="400" ></v-img>
        </v-card>

      </v-card>
    </v-container>

  </div>
</template>

<script>
// @ is an alias to /src

export default {
  name: 'ImageClassification',

  data () {
    return {
      drawer: true,
      space: " ",
      cards: [
        { title: 'Pre-fab homes', src: 'https://cdn.vuetifyjs.com/images/cards/house.jpg', flex: 12 },
        { title: 'Favorite road trips', src: 'https://cdn.vuetifyjs.com/images/cards/road.jpg', flex: 6 },
        { title: 'Best airlines', src: 'https://cdn.vuetifyjs.com/images/cards/plane.jpg', flex: 6 },
      ],
      sidebarMenu: true,
      toggleMini: false,
      items: [
        { title:"Home", href:"/", icon:"mdi-home-outline" },
        { title:"Detections", href:"/detections", icon:"mdi-shield-account" },
        { title:"Components", href:"/comp", icon:"mdi-palette-swatch" },
        { title:"Customers", href:"/customers", icon:"mdi-account-search-outline" },
        { title:"Orders", href:"/orders", icon:"mdi-bus-clock" },
        { title:"Settings", href:"/settings", icon:"mdi-settings-outline" },
      ],
      color: 'teal',
      right: false,
      permanent: true,
      miniVariant: false,
      expandOnHover: false,
      background: false,
    }
  },
}
</script>

<style lang="css">
  
.fade-enter-active, .fade-leave-active {
  transition-property: opacity;
  transition-duration: .25s;
}

.fade-enter-active {
  transition-delay: .25s;
}

.fade-enter, .fade-leave-active {
  opacity: 0
}

.theme--light.v-application ::-webkit-scrollbar {
  width: 13px;
}

.theme--light.v-application ::-webkit-scrollbar-track {
  background: #e6e6e6;
  border-left: 1px solid #dadada;
}

.theme--light.v-application ::-webkit-scrollbar-thumb {
  background: #b0b0b0;
  border: solid 3px #e6e6e6;
  border-radius: 7px;
}

.theme--light.v-application ::-webkit-scrollbar-thumb:hover {
  background: black;
}

.theme--dark.v-application ::-webkit-scrollbar {
  width: 13px;
}

.theme--dark.v-application ::-webkit-scrollbar-track {
  background: #202020;
  border-left: 1px solid #2c2c2c;
}

.theme--dark.v-application ::-webkit-scrollbar-thumb {
  background: #3e3e3e;
  border: solid 3px #202020;
  border-radius: 7px;
}

.theme--dark.v-application ::-webkit-scrollbar-thumb:hover {
  background: white;
}
</style>