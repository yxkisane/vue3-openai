<template>
<OpenAI/>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import OpenAI from '@/components/OpenAI.vue'; // @ is an alias to /src

export default defineComponent({
  name: 'HomeView',
  components: {
    OpenAI,
  },
});
</script>
