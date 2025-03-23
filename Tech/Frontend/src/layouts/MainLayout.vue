<template>
  <q-layout view="lHh Lpr lFf">
    <q-header elevated>
      <q-toolbar>
        <q-btn
          flat
          dense
          round
          icon="menu"
          aria-label="Menu"
          @click="toggleLeftDrawer"
        />

        <q-toolbar-title>
          S7 NSU Hackaton
        </q-toolbar-title>

        <div>Команда<br>Турбулентный профиль</div>
      </q-toolbar>
    </q-header>

    <q-drawer
      v-model="leftDrawerOpen"
      show-if-above
      bordered
    >
      <q-list>
        <q-item-label
          header
        >
          Хакатон НГУ-S7
        </q-item-label>

        <EssentialLink/>
      </q-list>
    </q-drawer>

    <q-page-container>
      <router-view />
    </q-page-container>

    
    <q-footer elevated>ready</q-footer>
  </q-layout>
</template>

<script setup lang="ts">
import { ref } from 'vue';

const leftDrawerOpen = ref(false);

function toggleLeftDrawer () {
  leftDrawerOpen.value = !leftDrawerOpen.value;
}
</script>
